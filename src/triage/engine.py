"""
Core orchestration for the baseline triage engine (v0.1).

Design target:
- Non-clinical users
- Deterministic, auditable, explainable
- Always escalate to human contact for intermediate/high

This baseline is intentionally simple (lexicon substring hits).

v0.2 trace layer (certification-oriented, still deterministic):
- decision_id (uuid4 per row)
- timestamp_utc (one timestamp per run)
- input_hash (sha256 of raw input text)
- lexicon_hash (sha256 of normalized lexicon terms)
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import List
import hashlib
import uuid

import pandas as pd

from triage.lexicon import normalize_terms

ENGINE_VERSION = "0.2.0"


@dataclass(frozen=True)
class RiskPolicy:
    """
    v0.x escalation policy for non-clinical users.

    Rule A:
    - intermediate/high -> always requires human contact
    """
    low_action: str = (
        "Low risk signal. Monitor symptoms. If symptoms worsen or you are concerned, "
        "contact a healthcare professional."
    )
    intermediate_action: str = (
        "Intermediate risk signal. Contact a healthcare professional as soon as possible."
    )
    high_action: str = (
        "High risk signal. Seek urgent medical attention immediately. "
        "Call emergency services if necessary."
    )

    safety_notice: str = (
        "This is an experimental research/prototype system. It does not diagnose or treat. "
        "Do not use it as a substitute for professional medical judgment."
    )


def _sha256_text(value: str) -> str:
    s = "" if value is None else str(value)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _lexicon_hash(terms: List[str]) -> str:
    # Normalize the serialized representation for deterministic hashing
    payload = "\n".join(sorted(set([t for t in terms if t]))).strip()
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def find_matched_terms(text: str, terms: List[str]) -> List[str]:
    """
    Return lexicon terms present in text using simple substring matching (v0.x).
    """
    s = str(text).lower()
    return [t for t in terms if t and (t in s)]


def hits_to_risk_level(hits: int) -> str:
    """
    v0.x mapping: count hits -> risk level.
    """
    if hits >= 2:
        return "high"
    if hits == 1:
        return "intermediate"
    return "low"


def apply_policy(risk_level: str, policy: RiskPolicy) -> tuple[bool, str]:
    """
    Return (requires_human_contact, recommended_action) for the given risk_level.
    """
    if risk_level == "high":
        return True, policy.high_action
    if risk_level == "intermediate":
        return True, policy.intermediate_action
    return False, policy.low_action


def run_baseline(
    notes_path: Path,
    lexicon_path: Path,
    out_path: Path,
    text_column: str = "triage_note",
    policy: RiskPolicy | None = None,
) -> pd.DataFrame:
    """
    Run baseline engine and write predictions to out_path.

    Output contract (v0.2):
    - engine_version
    - decision_id
    - timestamp_utc
    - input_hash
    - lexicon_hash
    - risk_level
    - risk_score (hits)
    - detected_red_flags (pipe-separated terms)
    - requires_human_contact
    - recommended_action
    - safety_notice
    """
    policy = policy or RiskPolicy()

    notes = pd.read_csv(notes_path)
    lexicon = pd.read_csv(lexicon_path)

    if text_column not in notes.columns:
        raise ValueError(f"notes is missing required column: '{text_column}'")
    if "term" not in lexicon.columns:
        raise ValueError("lexicon is missing required column: 'term'")

    terms = normalize_terms(lexicon)
    run_ts = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    lex_hash = _lexicon_hash(terms)

    notes = notes.copy()

    # Trace fields (deterministic except for uuid, which is explicitly for traceability)
    notes["engine_version"] = ENGINE_VERSION
    notes["timestamp_utc"] = run_ts
    notes["lexicon_hash"] = lex_hash
    notes["input_hash"] = notes[text_column].apply(_sha256_text)
    notes["decision_id"] = [str(uuid.uuid4()) for _ in range(len(notes))]

    # Detection + scoring
    notes["_matched_terms"] = notes[text_column].apply(lambda t: find_matched_terms(t, terms))
    notes["risk_score"] = notes["_matched_terms"].apply(len)
    notes["risk_level"] = notes["risk_score"].apply(hits_to_risk_level)

    # Policy outputs
    policy_out = notes["risk_level"].apply(lambda r: apply_policy(r, policy))
    notes["requires_human_contact"] = policy_out.apply(lambda x: x[0])
    notes["recommended_action"] = policy_out.apply(lambda x: x[1])

    # Explainability / trace
    notes["detected_red_flags"] = notes["_matched_terms"].apply(lambda xs: "|".join(xs))
    notes["safety_notice"] = policy.safety_notice

    # Cleanup internal column
    notes.drop(columns=["_matched_terms"], inplace=True)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    notes.to_csv(out_path, index=False)

    return notes
