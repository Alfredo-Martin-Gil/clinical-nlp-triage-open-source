"""
Core orchestration for the research baseline engine.

Design target:
- Offline research and software testing only
- Deterministic, auditable lexical signal detection
- Explicitly non-clinical outputs and conservative failure messaging

This baseline is intentionally simple (literal complete-word/phrase hits).

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
from triage.scoring import find_matched_terms as _find_matched_terms
from triage.scoring import predict_label_from_hits

ENGINE_VERSION = "0.3.0"
INTERPRETATION_BOUNDARY = (
    "Lexical signal-count output only; clinical risk is not established. "
    "Research use with synthetic data only. Not for patient decisions."
)


@dataclass(frozen=True)
class RiskPolicy:
    """
    Conservative research-output messaging.

    ``requires_human_contact`` is retained for backward compatibility and is
    always true so a zero-hit output cannot be interpreted as reassurance.
    """
    low_action: str = (
        "No configured lexicon signal detected. This does not establish low clinical risk. "
        "Do not use this output for patient decisions; clinical review is required for any "
        "real-world concern."
    )
    intermediate_action: str = (
        "One configured lexicon signal was detected. This is not a clinical risk estimate "
        "and must not be used for patient decisions."
    )
    high_action: str = (
        "Multiple configured lexicon signals were detected. This is not a clinical risk "
        "estimate and must not be used for patient decisions."
    )

    safety_notice: str = (
        "Experimental research prototype using synthetic data. It does not diagnose, "
        "triage or establish clinical risk. Do not use it for real-patient decisions."
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
    Backward-compatible wrapper around the authoritative scoring primitive.
    """
    return _find_matched_terms(text, terms)


def hits_to_risk_level(hits: int) -> str:
    """
    Backward-compatible mapping to the legacy technical signal-count band.
    """
    return predict_label_from_hits(hits)


def apply_policy(risk_level: str, policy: RiskPolicy) -> tuple[bool, str]:
    """
    Return conservative compatibility output and non-clinical message.
    """
    if risk_level == "high":
        return True, policy.high_action
    if risk_level == "intermediate":
        return True, policy.intermediate_action
    return True, policy.low_action


def run_baseline(
    notes_path: Path,
    lexicon_path: Path,
    out_path: Path,
    text_column: str = "triage_note",
    policy: RiskPolicy | None = None,
) -> pd.DataFrame:
    """
    Run baseline engine and write predictions to out_path.

    Output contract (v0.3):
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
    - signal_status
    - clinical_risk_established
    - negation_handling
    - lexicon_columns_used
    - interpretation_boundary
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
    notes["signal_status"] = notes["risk_score"].apply(
        lambda hits: "no_lexicon_signal_detected" if hits == 0 else "lexicon_signal_detected"
    )

    # Policy outputs
    policy_out = notes["risk_level"].apply(lambda r: apply_policy(r, policy))
    notes["requires_human_contact"] = policy_out.apply(lambda x: x[0])
    notes["recommended_action"] = policy_out.apply(lambda x: x[1])

    # Explainability / trace
    notes["detected_red_flags"] = notes["_matched_terms"].apply(lambda xs: "|".join(xs))
    notes["safety_notice"] = policy.safety_notice
    notes["clinical_risk_established"] = False
    notes["negation_handling"] = "not_implemented"
    notes["lexicon_columns_used"] = "term"
    notes["interpretation_boundary"] = INTERPRETATION_BOUNDARY

    # Cleanup internal column
    notes.drop(columns=["_matched_terms"], inplace=True)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    notes.to_csv(out_path, index=False)

    return notes
