"""
Evaluation utilities for rules_engine baseline.
"""

import pandas as pd


def compute_label_distribution(df: pd.DataFrame, column: str) -> pd.Series:
    """
    Compute label distribution for a prediction column.
    """
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")

    return df[column].value_counts()


def compute_basic_counts(df: pd.DataFrame) -> dict:
    """
    Return basic dataset statistics.
    """
    return {
        "rows": len(df),
        "columns": len(df.columns),
    }
