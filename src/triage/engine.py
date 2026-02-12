"""
Core orchestration for the baseline triage engine.

This module is intentionally CLI-free. It can be called from a script,
a notebook, or a workflow. The legacy CLI in src/rules_engine.py can be
rewired to call this module in a later step.
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd

from triage.lexicon import normalize_terms
from triage.scoring import count_hits, predict_label_from_hits


def run_baseline(
    notes_path: Path,
    lexicon_path: Path,
    out_path: Path,
    text_column: str = "triage_note",
) -> pd.DataFrame:
    """
    Run the baseline engine and write predictions to out_path.

    Returns the predictions DataFrame for programmatic use.
    """
    notes = pd.read_csv(notes_path)
    lexicon = pd.read_csv(lexicon_path)

    # Minimal schema validation (kept local to avoid dependency ambiguity)
    if text_column not in notes.columns:
        raise ValueError(f"notes is missing required column: '{text_column}'")
    if "term" not in lexicon.columns:
        raise ValueError("lexicon is missing required column: 'term'")

    terms = normalize_terms(lexicon)

    notes = notes.copy()
    notes["hits"] = notes[text_column].apply(lambda t: count_hits(t, terms))
    notes["predicted_category"] = notes["hits"].apply(predict_label_from_hits)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    notes.to_csv(out_path, index=False)

    return notes
