import unittest
import importlib.util
import sys
from pathlib import Path

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

    def test_engine_import_path_ok(self):
        # If this test runs, triage imports are working (smoke check).
        self.assertTrue(True)

    def test_scoring_module_smoke(self):
        from triage.scoring import predict_label_from_hits
        self.assertEqual(predict_label_from_hits(0), "low")
        self.assertEqual(predict_label_from_hits(1), "intermediate")
        self.assertEqual(predict_label_from_hits(2), "high")

    def test_lexicon_normalize_smoke(self):
        from triage.lexicon import normalize_terms
        df = pd.DataFrame({"term": [" Pain ", "pain", None, "Shock", "shock"]})
        terms = normalize_terms(df)
        self.assertIn("pain", terms)
        self.assertIn("shock", terms)
        self.assertEqual(len(terms), 2)


if __name__ == "__main__":
    unittest.main()
