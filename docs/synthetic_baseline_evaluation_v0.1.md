# Synthetic Baseline Evaluation Report — v0.1

## 1. Purpose

This report characterizes the behaviour of the repository's deterministic
baseline on its own synthetic dataset. It is designed to expose coverage gaps,
error patterns, and documentation–implementation inconsistencies.

This report is **not clinical validation** and provides no evidence of safety,
effectiveness, generalizability, or fitness for patient care.

## 2. Evaluated version

- Repository: `Alfredo-Martin-Gil/clinical-nlp-triage-open-source`
- Branch: `main`
- Commit: `0fa660b78992d4450ecd8e4f57569970e6057403`
- Engine version emitted by code: `0.2.0`
- Evaluation date: 2026-08-07
- Dataset: `data/notes_synthetic.csv`
- Lexicon: `data/lexicon_redflags.csv`
- Cases: 180
- Data status: synthetic English-language text with project-assigned labels

## 3. Implemented logic evaluated

The authoritative engine lowercases text, matches lexicon terms by substring,
counts matches, and assigns internal output bands:

- 0 hits → `low`;
- 1 hit → `intermediate`;
- 2 or more hits → `high`.

The engine does not use lexicon weights and does not implement negation,
temporal reasoning, history interpretation, semantic matching, or a validated
uncertainty model.

## 4. Reproduction commands

Run from the repository root:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -p "test_*.py" -v
python src/rules_engine.py --notes data/notes_synthetic.csv --lexicon data/lexicon_redflags.csv --out outputs/predictions.csv
python scripts/evaluate_synthetic_baseline.py --predictions outputs/predictions.csv --json-out outputs/synthetic_metrics.json --entity-csv outputs/synthetic_by_entity.csv --errors-csv outputs/synthetic_errors.csv
```

The five available tests passed during the 2026-08-07 reproduction. They test
software contracts and smoke behaviour, not clinical validity.

## 5. Main results

| Metric | Result |
|---|---:|
| Total synthetic cases | 180 |
| Exact-band agreement | 65/180 (36.1%) |
| Synthetic `high` cases | 84 |
| Exact-band sensitivity for synthetic `high` | 10/84 (11.9%) |
| Synthetic `high` predicted `intermediate` | 36/84 (42.9%) |
| Synthetic `high` predicted `low` | 38/84 (45.2%) |
| Cases with zero hits | 106/180 (58.9%) |
| Zero-hit cases labelled `high` | 38 |
| Predicted `high` when reference was not `high` | 1 |

Accuracy is reported for completeness but is not an adequate safety metric.
The primary technical concern is the large number of synthetic high-risk labels
mapped to a low internal band.

## 6. Confusion matrix

| Project-assigned label | Predicted `high` | Predicted `intermediate` | Predicted `low` |
|---|---:|---:|---:|
| `high` | 10 | 36 | 38 |
| `intermediate` | 1 | 21 | 34 |
| `low` | 0 | 6 | 34 |

Prediction distribution: 11 `high`, 63 `intermediate`, and 106 `low`.

## 7. Entity-level analysis

| Entity | Cases | Accuracy | Synthetic `high` | `high`→`high` | `high`→`low` | High sensitivity | Zero-hit cases |
|---|---:|---:|---:|---:|---:|---:|---:|
| abdominal_pain | 20 | 35% | 9 | 0 | 4 | 0% | 13 |
| allergic_reaction | 20 | 40% | 9 | 0 | 8 | 0% | 17 |
| altered_mental_status | 20 | 25% | 9 | 0 | 7 | 0% | 12 |
| back_pain | 20 | 25% | 8 | 0 | 6 | 0% | 18 |
| chest_pain | 20 | 30% | 10 | 1 | 3 | 10% | 13 |
| dyspnea | 20 | 60% | 8 | 4 | 1 | 50% | 2 |
| sepsis | 20 | 60% | 8 | 4 | 2 | 50% | 8 |
| stroke | 20 | 25% | 11 | 1 | 4 | 9.1% | 12 |
| syncope | 20 | 25% | 12 | 0 | 3 | 0% | 11 |

The lexicon contains terms for only part of the dataset's phrasing and does not
provide coherent coverage for several entities. Entity comparisons are
descriptive only because the synthetic cases and labels were not independently
designed or adjudicated.

## 8. Representative error analysis

Examples of synthetic `high` cases mapped to `low` with zero hits include:

- “Patient collapsed while walking upstairs” (`syncope`);
- “Crushing chest pain” (`chest_pain`);
- “Severe respiratory distress” (`dyspnea`);
- “Altered mental status” (`sepsis`);
- “Sudden right arm weakness” (`stroke`);
- “Anaphylaxis after bee sting” (`allergic_reaction`);
- “Unresponsive patient” (`altered_mental_status`);
- “Back pain with urinary retention” (`back_pain`).

The single non-`high` reference case predicted `high` was “Dyspnea with fever”:
both `dyspnea` and `fever` matched, producing two hits.

These examples show limitations of exact lexical coverage and the clinical
meaninglessness of hit count without contextual validation.

## 9. Known risks

- zero hits are converted to a `low` band rather than an unknown/unsupported
  state;
- the generated low-band action may be interpreted as reassurance;
- substring matching does not understand negation, timing, severity, history,
  or synonyms;
- the `weight` column creates an appearance of weighted scoring although it is
  unused;
- internal labels resemble clinical risk levels;
- test coverage does not assess clinical concepts or critical false negatives;
- project-assigned labels are not an independent reference standard.

## 10. Permitted interpretation

The results may be used to say that:

- the baseline runs on the supplied synthetic dataset;
- its software contract tests pass;
- outputs are traceable at the implemented level;
- the current lexical baseline has major coverage and failure-behaviour gaps;
- the repository demonstrates an explicit audit and corrective-documentation
  process.

## 11. Prohibited interpretation

The results must not be used to claim:

- validated clinical AI;
- safe or effective triage;
- sensitivity or accuracy in patients;
- improved outcomes or reduced risk;
- deployment or implementation in clinical settings;
- regulatory readiness, compliance, or medical-device status.

## 12. Criteria before a new technical version

Before presenting a new baseline as improved:

1. freeze the dataset, lexicon, expected outputs, and analysis plan;
2. define the output construct and an unknown/unsupported state;
3. reconcile lexicon coverage with every included entity;
4. add tests for critical false negatives, negation, substrings, synonyms,
   missing information, and temporal language;
5. separate development and locked test cases;
6. publish the full confusion matrix and error analysis;
7. document any label-review process;
8. avoid patient-facing language until evidence and governance justify it.

## 13. Validation boundary

This report is a technical evaluation on synthetic repository data. It is not a
clinical study, clinical validation, medical-device evaluation, or authorization
for real-world use.
