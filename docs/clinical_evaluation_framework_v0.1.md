# Proposed Evaluation Plan and Evidence Boundaries — v0.1

## Status

This is a proposed research evaluation plan. It is not a completed clinical
evaluation, validation protocol, or statement of alignment with regulatory
requirements.

The only completed evaluation in this version is a technical reproduction on
180 repository-provided synthetic notes. Results are documented in
`synthetic_baseline_evaluation_v0.1.md`.

## Current evaluation objective

Characterize what the deterministic baseline does, where its lexicon and rules
fail, and whether documentation matches implementation. Current synthetic
testing cannot establish clinical validity, generalizability, safety,
effectiveness, or benefit.

## Track A — synthetic technical evaluation

### Required case fields

- synthetic case ID;
- entity/category;
- synthetic text;
- project-assigned reference band;
- reference rationale and author/reviewer status;
- expected matched concepts;
- known ambiguity or missing information.

### Required metrics

- full confusion matrix;
- distribution of internal output bands;
- exact-band sensitivity for synthetic `high` labels;
- `high`→`low` count and rate;
- zero-hit count and zero-hit `high` cases;
- entity-level performance;
- representative false-negative and false-positive analysis;
- version, dataset hash, lexicon hash, and command used.

### Interpretation

Synthetic results are technical characterization only. Project-assigned labels
are not an independent clinical reference standard.

## Track B — future reference-standard development

Before retrospective patient data are considered, future work would need:

- a clearly defined use case and output construct;
- eligibility and exclusion criteria;
- a clinically justified annotation manual;
- independent reviewers and adjudication;
- inter-rater agreement analysis;
- a frozen dataset and pre-specified analysis plan;
- privacy, ethics, legal, security, and institutional approvals.

This track has not started.

## Track C — future retrospective evaluation

Any retrospective evaluation would require an authorized, representative
dataset and a reference standard appropriate to the intended use. Metrics would
be selected before analysis and could include sensitivity, specificity,
predictive values, calibration where applicable, subgroup error analysis, and
missed-critical-event analysis.

No retrospective patient-data evaluation has been completed.

## Track D — future human-factors evaluation

Human oversight claims require evidence about:

- warning comprehension;
- automation bias and over-trust;
- response to missing data and uncertainty;
- workload and interruption effects;
- escalation behaviour;
- error recovery and safe abandonment.

No usability or human-factors study has been completed.

## Acceptance criteria

No clinical acceptance threshold is defined for v0.x. A future protocol must
pre-specify thresholds based on the output construct, intended use, error costs,
and clinical/regulatory review. Thresholds must not be selected after seeing
results.

The current 38 synthetic `high`→`low` errors are a technical blocker for any
patient-facing or clinical-support interpretation.

## Governance

Evaluation artifacts should be version-controlled and linked to the exact code,
dataset, lexicon, and configuration. Documentation must not describe a proposed
test, control, or threshold as completed evidence.

Real-world research or deployment requires separate authorization and cannot be
inferred from this plan.
