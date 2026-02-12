from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Evaluate baseline predictions (optional ground truth).")
    p.add_argument("--predictions", required=True, type=Path, help="CSV produced by baseline engine")
    p.add_argument("--pred_col", default="predicted_label", help="Prediction column name")
    p.add_argument("--truth_col", default="label", help="Ground-truth column name (if present)")
    return p


def main() -> int:
    args = build_parser().parse_args()
    df = pd.read_csv(args.predictions)

    if args.pred_col not in df.columns:
        raise SystemExit(f"Missing prediction column: {args.pred_col}")

    print("Rows:", len(df))
    print("\nPrediction distribution:")
    print(df[args.pred_col].value_counts(dropna=False).to_string())

    if args.truth_col in df.columns:
        truth = df[args.truth_col].astype(str)
        pred = df[args.pred_col].astype(str)

        acc = (truth == pred).mean()
        print("\nGround truth detected:", args.truth_col)
        print("Accuracy:", round(float(acc), 4))

        print("\nConfusion matrix:")
        cm = pd.crosstab(truth, pred, rownames=["truth"], colnames=["pred"], dropna=False)
        print(cm.to_string())
    else:
        print(f"\nNo ground truth column '{args.truth_col}' found. Skipping accuracy/confusion matrix.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
