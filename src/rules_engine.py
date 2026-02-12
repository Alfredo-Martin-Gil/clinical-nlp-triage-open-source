from __future__ import annotations

import argparse
from pathlib import Path

from triage.engine import run_baseline


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Baseline rules engine: lexicon hits -> risk label"
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
        help="Path to notes CSV (must include required text column)",
    )
    p.add_argument(
        "--out",
        required=True,
        type=Path,
        help="Output CSV path",
    )
    return p


def main() -> int:
    args = build_parser().parse_args()

    # NOTE: engine expects a text column name; current dataset may vary by schema.
    # We default to the historical baseline column name used in this CLI: "text".
    run_baseline(
        notes_path=args.notes,
        lexicon_path=args.lexicon,
        out_path=args.out,
        text_column="text",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
