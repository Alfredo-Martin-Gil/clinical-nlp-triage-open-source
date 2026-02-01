from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd


REQUIRED_LEXICON_COLS = {"term"}
REQUIRED_NOTES_COLS = {"id", "text", "entity"}


def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def require_columns(df: pd.DataFrame, required: set[str], name: str) -> None:
    missing = required - set(df.columns)
    if missing:
        raise ValueError(
            f"[{name}] Missing required columns: {sorted(missing)}. Found: {list(df.columns)}"
        )


def normalize_terms(lexicon: pd.DataFrame) -> list[str]:
    terms = (
        lexicon["term"]
        .dropna()
        .astype(str)
        .str.strip()
        .str.lower()
    )
    return sorted({t for t in terms.tolist() if t})


def count_hits(text: str, terms: list[str]) -> int:
    s = str(text).lower()
    return sum(1 for t in terms if t in s)


def predict_label_from_hits(hits: int) -> str:
    if hits >= 2:
        return "high"
    if hits == 1:
        return "intermediate"
    return "low"


def run(lexicon_path: Path, notes_path: Path, output_path: Path) -> None:
    lexicon = load_csv(lexicon_path)
    notes = load_csv(notes_path)

    require_columns(lexicon, REQUIRED_LEXICON_COLS, "lexicon")
    require_columns(notes, REQUIRED_NOTES_COLS, "notes")

    terms = normalize_terms(lexicon)

    notes["hits_count"] = notes["text"].apply(lambda x: count_hits(x, terms))
    notes["predicted_label"] = notes["hits_count"].apply(predict_label_from_hits)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    notes[["id", "text", "entity", "hits_count", "predicted_label"]].to_csv(
        output_path,
        index=False
    )

    print(f"Saved: {output_path}")
    print("Label distribution:")
    print(notes["predicted_label"].value_counts(dropna=False).to_string())
    print("\nTop entities (high count):")
    print(
        notes.loc[notes["predicted_label"] == "high", "entity"]
        .value_counts()
        .head(10)
        .to_string()
    )


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Baseline rules engine: lexicon hits -> risk label"
    )
    p.add_argument(
        "--lexicon",
        required=True,
        type=Path,
        help="Path to lexicon CSV (must include column: term)"
    )
    p.add_argument(
        "--notes",
        required=True,
        type=Path,
        help="Path to notes CSV (must include: id,text,entity)"
    )
    p.add_argument(
        "--out",
        required=True,
        type=Path,
        help="Output CSV path"
    )
    return p


if __name__ == "__main__":
    args = build_parser().parse_args()
    run(args.lexicon, args.notes, args.out)
