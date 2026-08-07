# Research Hazard Register — v0.1

## Status and scope

This is a preliminary hazard-identification artifact for an offline research
prototype using synthetic text. It is not a completed risk-management file,
safety case, benefit-risk assessment, or authorization for patient use.

There is no current intended patient population, clinical user, deployment
setting, or remote/non-clinician use case.

## Observed and foreseeable hazards

| Hazard | Current evidence | Present control | Evidence gap |
|---|---|---|---|
| Missed configured signal | 38/84 synthetic `high` cases have zero hits | Explicit no-signal and no-clinical-risk boundary | Lexical coverage, independent labels, clinical evaluation |
| False reassurance | v0.2 attached monitoring language to zero hits | v0.3 removes reassurance and makes review metadata conservative | Human-factors testing and removal of legacy risk-like labels |
| Context error | Literal matching does not interpret negation, history, timing or severity | Limitation is machine-readable and documented | Tested contextual model and governed evaluation |
| Incidental substring match | Possible in v0.2 | v0.3 complete-word/phrase boundaries plus test | Broader multilingual/tokenization tests |
| Misleading weighted-scoring appearance | Lexicon contains unused `weight` | Output states only `term` is used | Schema redesign or tested weighting rationale |
| Public-code misuse | Repository is publicly accessible | Prominent prohibited-use language | Misuse monitoring and organizational controls are absent |

## Current risk conclusion

Residual clinical risk has not been estimated or accepted. Documentation and
human oversight do not make the prototype suitable for patient care. No
positive claim of safety, effectiveness, clinical validity, or acceptable risk
is supported.

## Future work

Any future study involving users or patient data would require a defined
context of use, accountable sponsor, ethics/privacy review, verified hazard
controls, independent clinical evaluation, human-factors testing, security
assessment, and jurisdiction-specific regulatory analysis.
