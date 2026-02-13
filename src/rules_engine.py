from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from triage.engine import run_baseline


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Baseline risk escalation engine (v0.x): lexicon hits -> risk escalation outputs"
    )
    p.add_argument(
        "--lexicon",
        required=True,
        type=Path,
        help="Path to lexicon CSV (must include column: term)",
    )
    p.add_argument(
        "--notes",
        required=True,
        type=Path,
        help="Path to notes CSV",
    )
    p.add_argument(
        "--out",
        required=True,
        type=Path,
        help="Output CSV path",
    )
    p.add_argument(
        "--text-column",
        default="triage_note",
        help="Text column name in notes CSV (default: triage_note)",
    )
    return p


def _resolve_text_column(notes_path: Path, requested: str) -> str:
    """
    Resolve the effective text column for the CLI.

    Policy:
    - Official column is 'triage_note'
    - For backward compatibility with existing datasets/CI smoke:
      if requested column is missing and 'text' exists, fall back to 'text'
    """
    try:
        df_head = pd.read_csv(notes_path, nrows=1)
    except Exception as e:
        raise RuntimeError(f"Failed to read notes CSV: {notes_path}") from e

    cols = set(df_head.columns)

    if requested in cols:
        return requested

    if requested == "triage_note" and "text" in cols:
        return "text"

    raise ValueError(
        f"notes is missing required column: '{requested}'. Available columns: {sorted(cols)}"
    )


def main() -> int:
    args = build_parser().parse_args()

    effective_text_col = _resolve_text_column(args.notes, args.text_column)

    run_baseline(
        notes_path=args.notes,
        lexicon_path=args.lexicon,
        out_path=args.out,
        text_column=effective_text_col,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
