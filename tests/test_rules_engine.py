import unittest
import importlib.util
import sys
from pathlib import Path
import tempfile

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

    def test_run_baseline_outputs_contract_v01(self):
        from triage.engine import run_baseline

        with tempfile.TemporaryDirectory() as td:
            td_path = Path(td)

            notes_path = td_path / "notes.csv"
            lexicon_path = td_path / "lexicon.csv"
            out_path = td_path / "predictions.csv"

            # Minimal v0.1 schema
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
                "risk_level",
                "risk_score",
                "detected_red_flags",
                "requires_human_contact",
                "recommended_action",
                "safety_notice",
            }
            self.assertTrue(expected_cols.issubset(set(df.columns)))

            # Policy A: intermediate/high -> human contact
            self.assertEqual(df.loc[0, "risk_level"], "low")
            self.assertFalse(bool(df.loc[0, "requires_human_contact"]))

            self.assertEqual(df.loc[1, "risk_level"], "intermediate")
            self.assertTrue(bool(df.loc[1, "requires_human_contact"]))

            self.assertEqual(df.loc[2, "risk_level"], "high")
            self.assertTrue(bool(df.loc[2, "requires_human_contact"]))

            self.assertTrue(out_path.exists())


if __name__ == "__main__":
    unittest.main()
