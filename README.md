# Clinical NLP Triage — Open-Source Research Prototype

## Project status

This repository contains an **early-stage, open-source research prototype** for
auditable clinical risk-signal detection in synthetic free-text notes.

The current baseline is deterministic and inspectable. It is intended to support
technical evaluation, clinical error analysis, documentation practice, and
discussion of human oversight. It is **not a validated triage system, clinical
decision-support product, medical device, or patient-care tool**.

> **Safety boundary**
>
> This repository must not be used to assess, triage, diagnose, treat, reassure,
> or provide instructions for a real patient. All current benchmark data are
> synthetic. No clinical deployment or patient use has occurred.

## Clinical problem explored

Emergency and prehospital workflows often involve incomplete information,
time pressure, unstructured symptom narratives, and handoffs. This project
explores how a transparent rules baseline can make candidate risk terms and
its own decision path visible for audit.

The project does not demonstrate that automated extraction improves decisions,
reduces cognitive load, prevents harm, or produces safe triage.

## What is implemented

The authoritative implementation is:

- `src/triage/engine.py` — core baseline engine;
- `src/rules_engine.py` — command-line interface;
- `data/notes_synthetic.csv` — 180 synthetic English-language notes with
  project-assigned labels;
- `data/lexicon_redflags.csv` — English-language term list;
- `tests/test_rules_engine.py` — five software contract/smoke tests;
- `.github/workflows/ci.yml` — unit-test and baseline-smoke workflow;
- `docs/synthetic_baseline_evaluation_v0.1.md` — current synthetic benchmark
  report and interpretation limits.

### Current scoring logic

For each note, the baseline:

1. converts the text to lowercase;
2. identifies lexicon terms by simple substring matching;
3. counts matched terms;
4. maps the number of hits to an internal output band:
   - 0 hits → `low`;
   - 1 hit → `intermediate`;
   - 2 or more hits → `high`;
5. records matched terms, hashes, timestamp, engine version, and a decision ID.

The current engine **does not implement** lexicon weighting, negation handling,
temporal reasoning, past-history interpretation, semantic matching, or a
validated uncertainty model. The `weight` column in the lexicon is not used by
the authoritative engine.

The output bands are experimental project categories. They are not validated
clinical triage levels and must not be interpreted as evidence that a patient is
at low, intermediate, or high clinical risk.

## Current synthetic benchmark

The baseline was reproduced against the 180 repository-provided synthetic notes
at commit `0fa660b78992d4450ecd8e4f57569970e6057403`.

| Technical observation | Result |
|---|---:|
| Overall exact-band agreement | 65/180 (36.1%) |
| Synthetic cases labelled `high` | 84 |
| `high` label predicted as `high` | 10/84 (11.9%) |
| `high` label predicted as `low` | 38/84 (45.2%) |
| Cases with zero lexicon hits | 106/180 (58.9%) |
| Zero-hit cases labelled `high` | 38 |

These results demonstrate major coverage and failure-behaviour limitations.
They do not constitute clinical performance estimates. See
`docs/synthetic_baseline_evaluation_v0.1.md` for the full confusion matrix,
entity-level analysis, and reproduction instructions.

## What the repository demonstrates

- translation of a clinical workflow problem into an inspectable prototype;
- deterministic execution and trace fields;
- use of synthetic data for technical stress testing;
- explicit documentation of hazards, limitations, and validation needs;
- separation between present evidence and future research proposals;
- a workflow for identifying and correcting documentation–implementation gaps.

## What is not demonstrated

- clinical validity, safety, effectiveness, or improved outcomes;
- reliable detection of high-risk cases;
- diagnostic, triage, treatment, or operational fitness;
- retrospective or prospective evaluation using real patient data;
- usability or human-factors validation;
- deployment in an ambulance service, emergency department, hospital, or
  remote-care environment;
- regulatory classification, clearance, certification, or compliance;
- a certified or operational quality management system;
- production readiness.

## Human oversight and use restrictions

Human responsibility is not a sufficient control for an unreliable model.
Accordingly, the present prototype is restricted to research, education,
software testing, and error analysis with synthetic data. Its generated
`recommended_action` field is experimental output and must not be followed for
patient care.

Any future clinical research would require a predefined protocol, appropriate
clinical and statistical review, representative data, ethics/privacy review,
independent reference standards, human-factors evaluation, and jurisdiction-
specific regulatory assessment.

## Documentation status

The documents under `docs/` and `qms/` are **draft research and governance
scaffolding**. They are not evidence that hazards are controlled, that residual
risk is acceptable, that the software conforms to a standard, or that a formal
QMS is operating.

Key documents:

- `docs/baseline_scoring.md` — implemented scoring logic;
- `docs/synthetic_baseline_evaluation_v0.1.md` — reproduced technical results;
- `docs/clinical_safety_case_v0.1.md` — draft safety argument and evidence gaps;
- `docs/context_of_use.md` — current research context and prohibited uses;
- `docs/regulatory_positioning_v0.1.md` — exploratory regulatory considerations;
- `qms/quality_management_system_overview_v0.1.md` — governance scaffolding;
- `docs/clinical_evaluation_framework_v0.1.md` — proposed evaluation plan.

## Reproduce the current baseline

From the repository root:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -p "test_*.py" -v
python src/rules_engine.py --notes data/notes_synthetic.csv --lexicon data/lexicon_redflags.csv --out outputs/predictions.csv
python scripts/evaluate_synthetic_baseline.py --predictions outputs/predictions.csv --json-out outputs/synthetic_metrics.json --entity-csv outputs/synthetic_by_entity.csv --errors-csv outputs/synthetic_errors.csv
```

The commands are for technical reproduction only. Generated outputs must not be
used for patient assessment.

## Related clinical and conceptual work

- [Prehospital Clinical Decision-Making Under Uncertainty](https://github.com/Alfredo-Martin-Gil/prehospital-clinical-decision-uncertainty)
  — clinical workflow foundation; not a protocol or algorithm.
- [Clinical Reflection Band](https://github.com/Alfredo-Martin-Gil/clinical-reflection-band)
  — research-stage conceptual architecture; no implemented or validated system.

## Licence

MIT. The licence permits software reuse but does not establish clinical fitness,
regulatory authorization, or safety.
