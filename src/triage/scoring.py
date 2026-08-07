"""
Single authoritative set of matching and scoring primitives for the baseline.

These functions produce lexical signal-count bands. They do not estimate
clinical risk and they do not implement negation, temporality, severity or
patient-context interpretation.
"""

from __future__ import annotations

import re


def find_matched_terms(text: str, terms: list[str]) -> list[str]:
    """Return configured terms matched as complete words/phrases.

    The boundary check prevents incidental substring matches such as ``pain``
    inside ``painting``. This is still literal matching: negated and historical
    mentions are not interpreted.
    """
    normalized_text = str(text).casefold()
    matches: list[str] = []
    for term in terms:
        normalized_term = str(term).strip().casefold()
        if not normalized_term:
            continue
        pattern = rf"(?<!\w){re.escape(normalized_term)}(?!\w)"
        if re.search(pattern, normalized_text):
            matches.append(normalized_term)
    return matches


def count_hits(text: str, terms: list[str]) -> int:
    """
    Count how many lexicon terms appear in the text.

    Baseline implementation uses complete-word/phrase literal matching.
    """
    return len(find_matched_terms(text, terms))


def predict_label_from_hits(hits: int) -> str:
    """
    Map hit count to the legacy technical signal-count band.

    The returned field remains named ``risk_level`` for output compatibility,
    but it must not be interpreted as clinical risk.
    """
    if hits >= 2:
        return "high"
    if hits == 1:
        return "intermediate"
    return "low"
