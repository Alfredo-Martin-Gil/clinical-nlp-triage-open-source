# Baseline Scoring — Implemented Logic v0.3.0

## Status and boundary

This document describes the authoritative baseline implemented in
`src/triage/scoring.py`, orchestrated by `src/triage/engine.py`, and exposed by
`src/rules_engine.py` in the C1-R2 branch.

It is a software-behaviour description, not a clinical specification. The
output bands are experimental project categories and must not be interpreted as
validated clinical risk or triage levels.

## Inputs

Notes require a text column. The CLI accepts `triage_note` and falls back to
`text` for the repository dataset. The lexicon requires a `term` column.

The repository dataset contains synthetic English-language notes. No real
patient data are included in the current benchmark.

## Matching logic

For each note, the engine:

1. performs case-insensitive normalization;
2. checks whether each normalized lexicon term occurs as a complete word or
   phrase using escaped regular-expression boundaries;
3. returns the set of matched lexicon terms.

The current implementation does not use semantic similarity, negation,
temporal context, patient history, or the lexicon `weight` field. Only the
lexicon `term` column affects detection and scoring.

## Score computation

`risk_score` equals the number of matched lexicon terms.

## Internal band mapping

- 0 hits → `low`;
- 1 hit → `intermediate`;
- 2 or more hits → `high`.

This mapping is an experimental software rule. It has not been shown to
represent clinical severity, urgency, or outcome risk.

## Output contract

The engine produces:

- `engine_version`;
- `decision_id`;
- `timestamp_utc`;
- `input_hash`;
- `lexicon_hash`;
- `risk_level`;
- `risk_score`;
- `detected_red_flags`;
- `requires_human_contact`;
- `recommended_action`;
- `safety_notice`;
- `signal_status`;
- `clinical_risk_established`;
- `negation_handling`;
- `lexicon_columns_used`;
- `interpretation_boundary`.

Trace fields support reproducibility and error analysis. They do not demonstrate
clinical explainability, safety, or accountability.

## Known failure behaviour

On the repository-provided 180-case synthetic set, 106 cases receive zero hits.
Thirty-eight of those zero-hit cases carry a project-assigned `high` label. For
backward compatibility, the engine still maps zero hits to the legacy `low`
band, but now emits `no_lexicon_signal_detected`, states that low clinical risk
is not established, and keeps conservative human-review metadata. This removes
the monitoring-oriented false-reassurance message; it does not repair lexical
coverage or establish clinical performance.

See `synthetic_baseline_evaluation_v0.1.md` for detailed results.

## Roadmap, not current functionality

The following are future technical proposals only:

- lexicon weighting;
- negation handling;
- temporal and history reasoning;
- matched-span metadata;
- replacement of legacy risk-like field names with a versioned signal-only schema;
- uncertainty gating;
- clinically reviewed escalation policies.

None should be described as implemented until code, tests, and evaluation
evidence exist in the same version.
