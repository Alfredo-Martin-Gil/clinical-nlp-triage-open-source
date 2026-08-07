import unittest
import importlib.util
import sys
from pathlib import Path
import tempfile
import re

import pandas as pd


def load_rules_engine_module():
    repo_root = Path(__file__).resolve().parents[1]

    # Ensure `src/` is importable so `import triage.*` works in CI.
    src_path = repo_root / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))

    engine_path = repo_root / "src" / "rules_engine.py"

    spec = importlib.util.spec_from_file_location("rules_engine", engine_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


RE = load_rules_engine_module()


class TestRulesEngineBaseline(unittest.TestCase):

    def test_parser_exists(self):
        self.assertTrue(hasattr(RE, "build_parser"))

    def test_cli_main_exists(self):
        self.assertTrue(hasattr(RE, "main"))

    def test_scoring_mapping_v01(self):
        from triage.engine import hits_to_risk_level
        self.assertEqual(hits_to_risk_level(0), "low")
        self.assertEqual(hits_to_risk_level(1), "intermediate")
        self.assertEqual(hits_to_risk_level(2), "high")

    def test_lexicon_normalize_smoke(self):
        from triage.lexicon import normalize_terms
        df = pd.DataFrame({"term": [" Pain ", "pain", None, "Shock", "shock"]})
        terms = normalize_terms(df)
        self.assertIn("pain", terms)
        self.assertIn("shock", terms)
        self.assertEqual(len(terms), 2)

    def test_run_baseline_outputs_contract_v02(self):
        from triage.engine import run_baseline

        with tempfile.TemporaryDirectory() as td:
            td_path = Path(td)

            notes_path = td_path / "notes.csv"
            lexicon_path = td_path / "lexicon.csv"
            out_path = td_path / "predictions.csv"

            # Minimal schema
            pd.DataFrame(
                {"triage_note": ["no issues", "chest pain", "chest pain + shock"]}
            ).to_csv(notes_path, index=False)

            pd.DataFrame(
                {"term": ["chest pain", "shock"]}
            ).to_csv(lexicon_path, index=False)

            df = run_baseline(
                notes_path=notes_path,
                lexicon_path=lexicon_path,
                out_path=out_path,
                text_column="triage_note",
            )

            expected_cols = {
                "engine_version",
                "decision_id",
                "timestamp_utc",
                "input_hash",
                "lexicon_hash",
                "risk_level",
                "risk_score",
                "detected_red_flags",
                "requires_human_contact",
                "recommended_action",
                "safety_notice",
                "signal_status",
                "clinical_risk_established",
                "negation_handling",
                "lexicon_columns_used",
                "interpretation_boundary",
            }
            self.assertTrue(expected_cols.issubset(set(df.columns)))

            # Basic sanity for trace fields
            self.assertTrue(df["decision_id"].astype(str).str.len().min() >= 32)
            self.assertTrue(df["input_hash"].astype(str).str.fullmatch(r"[0-9a-f]{64}").all())
            self.assertTrue(df["lexicon_hash"].astype(str).str.fullmatch(r"[0-9a-f]{64}").all())
            self.assertTrue(df["timestamp_utc"].astype(str).str.contains("Z|\\+00:00").all())

            # Conservative compatibility policy: zero hits never implies reassurance.
            self.assertEqual(df.loc[0, "risk_level"], "low")
            self.assertEqual(df.loc[0, "signal_status"], "no_lexicon_signal_detected")
            self.assertTrue(bool(df.loc[0, "requires_human_contact"]))
            self.assertFalse(bool(df.loc[0, "clinical_risk_established"]))
            self.assertIn("does not establish low clinical risk", df.loc[0, "recommended_action"])

            self.assertEqual(df.loc[1, "risk_level"], "intermediate")
            self.assertTrue(bool(df.loc[1, "requires_human_contact"]))

            self.assertEqual(df.loc[2, "risk_level"], "high")
            self.assertTrue(bool(df.loc[2, "requires_human_contact"]))

            # File written
            self.assertTrue(out_path.exists())

    def test_complete_word_matching_avoids_incidental_substrings(self):
        from triage.engine import find_matched_terms

        self.assertEqual(find_matched_terms("The patient is painting", ["pain"]), [])
        self.assertEqual(find_matched_terms("The patient reports pain", ["pain"]), ["pain"])

    def test_negated_mentions_are_detected_but_not_interpreted(self):
        from triage.engine import run_baseline

        with tempfile.TemporaryDirectory() as td:
            td_path = Path(td)
            notes_path = td_path / "notes.csv"
            lexicon_path = td_path / "lexicon.csv"
            out_path = td_path / "predictions.csv"
            pd.DataFrame({"triage_note": ["No chest pain"]}).to_csv(notes_path, index=False)
            pd.DataFrame({"term": ["chest pain"]}).to_csv(lexicon_path, index=False)

            row = run_baseline(notes_path, lexicon_path, out_path).iloc[0]
            self.assertEqual(row["risk_level"], "intermediate")
            self.assertEqual(row["negation_handling"], "not_implemented")
            self.assertFalse(bool(row["clinical_risk_established"]))
            self.assertIn("not a clinical risk estimate", row["recommended_action"])

    def test_unmatched_high_concern_text_does_not_reassure(self):
        from triage.engine import run_baseline

        with tempfile.TemporaryDirectory() as td:
            td_path = Path(td)
            notes_path = td_path / "notes.csv"
            lexicon_path = td_path / "lexicon.csv"
            out_path = td_path / "predictions.csv"
            pd.DataFrame({"triage_note": ["Patient collapsed while walking upstairs"]}).to_csv(
                notes_path, index=False
            )
            pd.DataFrame({"term": ["exertional syncope"]}).to_csv(lexicon_path, index=False)

            row = run_baseline(notes_path, lexicon_path, out_path).iloc[0]
            self.assertEqual(row["signal_status"], "no_lexicon_signal_detected")
            self.assertTrue(bool(row["requires_human_contact"]))
            self.assertIn("does not establish low clinical risk", row["recommended_action"])

    def test_weight_column_is_not_used_by_v03(self):
        from triage.engine import run_baseline

        with tempfile.TemporaryDirectory() as td:
            td_path = Path(td)
            notes_path = td_path / "notes.csv"
            lexicon_path = td_path / "lexicon.csv"
            out_path = td_path / "predictions.csv"
            pd.DataFrame({"triage_note": ["chest pain"]}).to_csv(notes_path, index=False)
            pd.DataFrame({"term": ["chest pain"], "weight": [999]}).to_csv(
                lexicon_path, index=False
            )

            row = run_baseline(notes_path, lexicon_path, out_path).iloc[0]
            self.assertEqual(row["risk_score"], 1)
            self.assertEqual(row["lexicon_columns_used"], "term")


if __name__ == "__main__":
    unittest.main()
