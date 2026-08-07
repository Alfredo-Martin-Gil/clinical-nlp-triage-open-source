# Draft Clinical Safety Argument and Evidence Gaps — v0.1

## Document status

This is a **research-stage safety argument template**. It is not a completed
safety case and does not establish that the prototype is safe, clinically
beneficial, fit for an intended use, or suitable for regulatory submission.

The present evidence supports only software traceability and synthetic error
analysis. It does not support claims of acceptable residual risk or risk
reduction.

## Current safety conclusion

No positive clinical safety claim can be made for the current baseline.

The repository-provided synthetic benchmark identified a material failure mode:
38 of 84 cases labelled `high` were assigned the internal `low` band. Exact-band
sensitivity for the synthetic `high` label was 10/84 (11.9%). These figures are
not clinical performance estimates, but they are sufficient to prohibit patient
use and to invalidate reassurance-oriented interpretations of zero-hit outputs.

## Restricted claim

The current defensible claim is:

> The repository documents an auditable research prototype and a structured
> process for identifying hazards, implementation–documentation gaps, and
> evidence requirements using synthetic data.

This claim does not imply that hazards are controlled.

## Candidate safety objectives for future research

Future versions may be evaluated against objectives such as:

1. avoid false reassurance when critical information is absent;
2. make uncertainty and missing information visible;
3. prevent unsupported low-risk interpretations;
4. maintain traceability between inputs, rules, outputs, and versions;
5. preserve human review without treating human oversight as a substitute for
   model performance;
6. define and test safe failure behaviour before any user-facing study.

These are proposed objectives, not achieved properties.

## Evidence map

| Topic | Evidence currently present | Evidence still required |
|---|---|---|
| Software traceability | Version, timestamp, input/lexicon hashes, decision ID | Independent verification and lifecycle controls |
| Software contract | Nine unit, boundary and smoke tests | Independent verification, broader contextual tests, regression suite |
| Synthetic performance | 180-case benchmark and error analysis | Frozen protocol, independent label review, representative case design |
| High-risk failure behaviour | 38 synthetic `high`→`low` errors identified | Corrective implementation and pre-specified acceptance criteria |
| Human oversight | Documentation statements | Usability, comprehension, workload and behavioural testing |
| Residual risk | None | Hazard-control verification and benefit–risk assessment |
| Clinical performance | None | Appropriately governed retrospective/prospective evidence |

## Open hazards

- lexical non-coverage producing zero hits;
- literal matching without negation, temporal, severity or history interpretation;
- no negation or temporal reasoning;
- unused lexicon weights;
- experimental bands that resemble clinical risk categories;
- legacy risk-like labels remain, although v0.3 removes monitoring-oriented
  zero-hit text and adds explicit no-signal boundaries;
- incomplete coverage across clinical entities;
- documentation that previously exceeded the implemented evidence;
- potential misuse of public code outside its research boundary.

## Human responsibility

The prototype must not be used for patient care. A human-in-the-loop statement
does not make an unvalidated system safe and does not transfer responsibility
away from developers, investigators, institutions, or users.

Any future human-factors claim requires evidence that intended users understand
warnings, do not over-trust outputs, and respond appropriately under realistic
workflow conditions.

## Conditions before a future safety case

A future safety case would require, at minimum:

- a defined and justified context of use;
- controlled requirements and configuration;
- verified hazard controls linked to implementation;
- a frozen evaluation protocol and acceptance criteria;
- independently reviewed reference labels;
- clinically relevant performance and error analysis;
- human-factors evidence;
- privacy, ethics, security, and jurisdiction-specific regulatory review;
- documented residual-risk and benefit–risk decisions by accountable parties.

## Regulatory boundary

This draft is not aligned evidence of conformity with ISO 14971, IEC 62304,
ISO 13485, IMDRF guidance, ANMAT requirements, or Health Canada requirements.
Those sources may inform future gap analysis only after intended use and product
claims are defined with qualified regulatory input.
