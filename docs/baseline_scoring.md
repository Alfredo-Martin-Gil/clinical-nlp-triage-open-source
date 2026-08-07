# Baseline Scoring — Implemented Logic v0.2.0

## Status and boundary

This document describes the authoritative baseline implemented in
`src/triage/engine.py` and exposed by `src/rules_engine.py` at commit
`0fa660b78992d4450ecd8e4f57569970e6057403`.

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

1. converts the note to lowercase;
2. checks whether each normalized lexicon term occurs as a substring;
3. returns the set of matched lexicon terms.

The current implementation does not use token boundaries, semantic similarity,
negation, temporal context, patient history, or the lexicon `weight` field.

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
- `safety_notice`.

Trace fields support reproducibility and error analysis. They do not demonstrate
clinical explainability, safety, or accountability.

## Known failure behaviour

On the repository-provided 180-case synthetic set, 106 cases receive zero hits.
Thirty-eight of those zero-hit cases carry a project-assigned `high` label. The
current engine maps zero hits to `low` and emits a monitoring-oriented action.
That behaviour is incompatible with patient use and is a documented technical
safety blocker.

See `synthetic_baseline_evaluation_v0.1.md` for detailed results.

## Roadmap, not current functionality

The following are future technical proposals only:

- lexicon weighting;
- negation handling;
- temporal and history reasoning;
- matched-span metadata;
- uncertainty gating;
- clinically reviewed escalation policies.

None should be described as implemented until code, tests, and evaluation
evidence exist in the same version.
