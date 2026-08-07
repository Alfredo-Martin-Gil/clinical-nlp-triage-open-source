from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


LEVELS = ["high", "intermediate", "low"]


def confusion_records(df: pd.DataFrame) -> list[dict[str, object]]:
    matrix = pd.crosstab(
        df["label"],
        df["risk_level"],
        rownames=["truth"],
        colnames=["prediction"],
        dropna=False,
    ).reindex(index=LEVELS, columns=LEVELS, fill_value=0)
    return [
        {
            "truth": truth,
            **{prediction: int(matrix.loc[truth, prediction]) for prediction in LEVELS},
        }
        for truth in LEVELS
    ]


def entity_records(df: pd.DataFrame) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for entity, group in df.groupby("entity", sort=True):
        high = group[group["label"] == "high"]
        records.append(
            {
                "entity": entity,
                "n": int(len(group)),
                "accuracy": round(float((group["label"] == group["risk_level"]).mean()), 4),
                "truth_high": int(len(high)),
                "high_predicted_high": int((high["risk_level"] == "high").sum()),
                "high_predicted_intermediate": int((high["risk_level"] == "intermediate").sum()),
                "high_predicted_low": int((high["risk_level"] == "low").sum()),
                "high_sensitivity": (
                    round(float((high["risk_level"] == "high").mean()), 4)
                    if len(high)
                    else None
                ),
                "zero_hit_cases": int((group["risk_score"] == 0).sum()),
            }
        )
    return records


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Evaluate repository-provided synthetic baseline outputs."
    )
    parser.add_argument("--predictions", required=True, type=Path)
    parser.add_argument("--json-out", required=True, type=Path)
    parser.add_argument("--entity-csv", required=True, type=Path)
    parser.add_argument("--errors-csv", required=True, type=Path)
    args = parser.parse_args()

    df = pd.read_csv(args.predictions)
    required = {"id", "text", "entity", "label", "risk_score", "risk_level"}
    missing = sorted(required - set(df.columns))
    if missing:
        raise SystemExit(f"Missing columns: {', '.join(missing)}")

    high = df[df["label"] == "high"]
    summary = {
        "dataset_type": "synthetic",
        "n": int(len(df)),
        "accuracy": round(float((df["label"] == df["risk_level"]).mean()), 4),
        "prediction_distribution": {
            level: int((df["risk_level"] == level).sum()) for level in LEVELS
        },
        "truth_distribution": {
            level: int((df["label"] == level).sum()) for level in LEVELS
        },
        "truth_high": int(len(high)),
        "high_sensitivity_exact_band": round(
            float((high["risk_level"] == "high").mean()), 4
        ),
        "high_predicted_low": int((high["risk_level"] == "low").sum()),
        "high_predicted_low_rate": round(
            float((high["risk_level"] == "low").mean()), 4
        ),
        "high_predicted_intermediate": int(
            (high["risk_level"] == "intermediate").sum()
        ),
        "high_predicted_intermediate_rate": round(
            float((high["risk_level"] == "intermediate").mean()), 4
        ),
        "zero_hit_cases": int((df["risk_score"] == 0).sum()),
        "zero_hit_truth_high": int(
            ((df["risk_score"] == 0) & (df["label"] == "high")).sum()
        ),
        "predicted_high_when_truth_not_high": int(
            ((df["label"] != "high") & (df["risk_level"] == "high")).sum()
        ),
        "confusion_matrix": confusion_records(df),
        "by_entity": entity_records(df),
        "interpretation_boundary": (
            "Technical characterization on repository-provided synthetic data; "
            "not clinical validation or evidence of safety/effectiveness."
        ),
    }

    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.entity_csv.parent.mkdir(parents=True, exist_ok=True)
    args.errors_csv.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    pd.DataFrame(summary["by_entity"]).to_csv(args.entity_csv, index=False)

    errors = df[df["label"] != df["risk_level"]].copy()
    errors["error_type"] = errors.apply(
        lambda row: f"{row['label']}->{row['risk_level']}", axis=1
    )
    errors[
        [
            "id",
            "entity",
            "text",
            "label",
            "risk_level",
            "risk_score",
            "detected_red_flags",
            "error_type",
        ]
    ].to_csv(args.errors_csv, index=False)

    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
