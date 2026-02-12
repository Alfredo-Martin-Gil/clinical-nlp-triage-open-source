"""
Scoring primitives for the baseline rules engine.
"""

from __future__ import annotations


def count_hits(text: str, terms: list[str]) -> int:
    """
    Count how many lexicon terms appear in the text.

    Baseline implementation uses substring matching.
    """
    s = str(text).lower()
    return sum(1 for t in terms if t in s)


def predict_label_from_hits(hits: int) -> str:
    """
    Map hit count to baseline risk label.
    """
    if hits >= 2:
        return "high"
    if hits == 1:
        return "intermediate"
    return "low"
