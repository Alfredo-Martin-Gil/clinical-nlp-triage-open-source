import unittest
import importlib.util
from pathlib import Path

import pandas as pd


def load_rules_engine_module():
    repo_root = Path(__file__).resolve().parents[1]
    engine_path = repo_root / "src" / "rules_engine.py"

    spec = importlib.util.spec_from_file_location("rules_engine", engine_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


RE = load_rules_engine_module()


class TestRulesEngineBaseline(unittest.TestCase):

    def test_require_columns_ok(self):
        df = pd.DataFrame({"a": [1], "b": [2]})
        RE.require_columns(df, {"a", "b"}, name="test_df")

    def test_require_columns_missing_raises(self):
        df = pd.DataFrame({"a": [1]})
        with self.assertRaises(ValueError):
            RE.require_columns(df, {"a", "b"}, name="test_df")

    def test_normalize_terms(self):
        df = pd.DataFrame({
            "term": [" Pain ", "pain", None, "Shock", "shock"]
        })
        terms = RE.normalize_terms(df)
        self.assertIn("pain", terms)
        self.assertIn("shock", terms)
        self.assertEqual(len(terms), 2)

    def test_count_hits(self):
        text = "Patient has chest pain."
        terms = ["pain"]
        hits = RE.count_hits(text, terms)
        self.assertEqual(hits, 1)

    def test_predict_label_thresholds(self):
        self.assertEqual(RE.predict_label_from_hits(0), "low")
        self.assertEqual(RE.predict_label_from_hits(1), "intermediate")
        self.assertEqual(RE.predict_label_from_hits(2), "high")


if __name__ == "__main__":
    unittest.main()
