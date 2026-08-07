# Uncertainty Model Proposal — v0.1

## Status

This is a conceptual proposal. The current engine does **not** compute an
uncertainty score or level, infer missing clinical data, block decisions based
on uncertainty, or integrate sensor/model confidence.

The implemented v0.3 fields are limited to:

- `signal_status` — whether configured lexicon terms were detected;
- `clinical_risk_established=false` — a fixed interpretation boundary;
- `negation_handling=not_implemented`;
- `interpretation_boundary` — research-only, no-patient-use statement.

These fields are not an uncertainty model.

## Candidate uncertainty sources for future research

- incomplete or ambiguous symptom text;
- lexical non-coverage;
- negation, temporal, severity and history context;
- conflicting structured and unstructured information;
- distribution shift and language variation;
- missing data and unreliable input channels.

## Candidate requirements

A future uncertainty mechanism would require a defined construct, traceable
drivers, pre-specified thresholds, conservative unsupported-output behaviour,
calibration and subgroup evaluation, and human-factors testing. Uncertainty
must not be converted into reassurance or presented as confidence without
supporting evidence.

## Prohibited interpretation

This proposal does not show that uncertainty is measured, controlled, visible
to users, or clinically meaningful. It must not be used to claim an implemented
uncertainty layer, safe failure behaviour, remote-use suitability, or clinical
readiness.
