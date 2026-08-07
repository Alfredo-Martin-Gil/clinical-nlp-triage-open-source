# C1-R2 Safety and Technical Coherence Record — v0.1

## Status

This record describes a proposed research-prototype revision. It is not a
clinical safety case, clinical evaluation, deployment record, or regulatory
artifact.

## Problem addressed

The audited v0.2 baseline converted zero configured-term hits to a legacy
`low` band, set `requires_human_contact=false`, and emitted monitoring language.
On the repository's 180 synthetic cases, 38 of 84 project-labelled `high`
cases had zero hits. The output could therefore be misread as reassurance even
though the engine had not established clinical risk.

## Implemented changes

- engine version advanced to `0.3.0`;
- zero-hit output now says no configured lexicon signal was detected and that
  low clinical risk is not established;
- compatibility field `requires_human_contact` is conservative for every band;
- `signal_status`, `clinical_risk_established`, `negation_handling`,
  `lexicon_columns_used`, and `interpretation_boundary` were added;
- matching now uses complete-word/phrase literal boundaries;
- scoring primitives have one authoritative implementation;
- tests expanded from five to nine;
- CI reproduces the synthetic evaluator and asserts its interpretation boundary.

## Deliberately not implemented

- no negation, temporality, history, severity, synonym, or semantic model;
- no use of lexicon weights;
- no new clinical escalation algorithm;
- no dataset relabelling or lexical additions targeted to benchmark cases;
- no patient-facing recommendation or clinical workflow.

## Verification

- nine software tests pass;
- the 180-case synthetic evaluator completes;
- band agreement remains 65/180 (0.3611);
- exact synthetic `high` sensitivity remains 10/84 (0.1190);
- 38/84 synthetic `high` cases remain in the legacy zero-hit/`low` band;
- `git diff --check` passes.

Unchanged band metrics are expected because the revision is not optimized
against the synthetic labels. The material improvement is removal of a
reassuring failure message and clearer, machine-readable interpretation limits.

## Remaining blockers

The legacy risk-like field names, weak lexical coverage, project-assigned
labels, absence of an unknown/unsupported primary schema, and lack of clinical
reference data remain unresolved. The prototype is not suitable for patient
use and has not been clinically validated.
