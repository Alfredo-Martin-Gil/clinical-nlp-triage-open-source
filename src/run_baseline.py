"""
Reproducible baseline execution script.

This script runs the rules_engine baseline without relying on Jupyter.
"""

from pathlib import Path
import pandas as pd

from triage.rules_engine import (
    require_columns,
    normalize_terms,
    count_hits,
    predict_label_from_hits,
)


def main():
    repo_root = Path(__file__).resolve().parents[1]

    data_path = repo_root / "data" / "notes_synthetic.csv"
    lexicon_path = repo_root / "data" / "lexicon_redflags.csv"
    output_path = repo_root / "outputs" / "predictions.csv"

    notes = pd.read_csv(data_path)
    lexicon = pd.read_csv(lexicon_path)

    require_columns(notes, {"triage_note"}, name="notes")
    require_columns(lexicon, {"term"}, name="lexicon")

    terms = normalize_terms(lexicon)

    notes["hits"] = notes["triage_note"].apply(
        lambda text: count_hits(text, terms)
    )

    notes["predicted_category"] = notes["hits"].apply(
        predict_label_from_hits
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    notes.to_csv(output_path, index=False)

    print("Baseline run complete.")
    print(notes["predicted_category"].value_counts())


if __name__ == "__main__":
    main()
