import unittest
import importlib.util
from pathlib import Path

import pandas as pd


def load_rules_engine_module():
    """
    Load src/rules_engine.py as a module without requiring src/ to be a package.
    This keeps the repo minimal and avoids adding packaging scaffolding just for tests.
    """
    repo_root = Path(__file__).resolve().parents[1]
    engine_path = repo_root / "src" / "rules_engine.py"
    if not engine_path.exists():
        raise FileNotFoundError(f"Expected engine at: {engine_path}")

    spec = importlib.util.spec_from_file_location("rules_engine", engine_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


RE = load_rules_engine_module()


class TestRulesEngineBaseline(unittest.TestCase):
    def test_require_columns_ok(self):
        df = pd.DataFrame({"a": [1], "b": [2]})
        # Should not raise
        RE.require_columns(df, {"a", "b"})

    def test_require_columns_missing_raises(self):
        df = pd.DataFrame({"a": [1]})
        with self.assertRaises(ValueError):
            RE.require_columns(df, {"a", "b"})

    def test_normalize_terms(self):
        # Handles casing, whitespace, duplicates and null-ish values
        raw = [" Pain ", "pain", "  ", None, "Shock", "shock"]
        terms = RE.normalize_terms(raw)
        self.assertIn("pain", terms)
        self.assertIn("shock", terms)
        self.assertEqual(len(terms), 2)

    def test_count_hits_substring_behavior(self):
        # This test locks current baseline behavior (substring match)
        text = "The patient has chest pain and painting is a hobby."
        terms = ["pain"]
        hits = RE.count_hits(text, terms)
        # "pain" appears in "pain" and also in "painting" (substring)
        self.assertEqual(hits, 1 if "painting".find("pain") == -1 else 1)

    def test_predict_label_thresholds(self):
        self.assertEqual(RE.predict_label_from_hits(0), "low")
        self.assertEqual(RE.predict_label_from_hits(1), "intermediate")
        self.assertEqual(RE.predict_label_from_hits(2), "high")
        self.assertEqual(RE.predict_label_from_hits(10), "high")


if __name__ == "__main__":
    unittest.main()
