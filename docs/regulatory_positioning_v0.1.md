# Regulatory Positioning – v0.1

## 1. Regulatory Intent

This document defines the preliminary regulatory positioning of the system described in this repository.

The system is being developed with the intention of future compliance with:

- ANMAT (Argentina)
- Health Canada (Canada)

The European Union regulatory framework is intentionally excluded from this design scope.

This document establishes the intended use, risk positioning hypothesis, and explicit exclusions in order to prevent regulatory ambiguity during early development phases.

---

## 2. Intended Use Statement (Preliminary)

The system is intended to provide structured clinical decision support in environments where immediate access to a licensed physician is not available.

The system:

- Assists in identifying high-risk clinical patterns.
- Highlights escalation criteria.
- Structures incomplete information.
- Suggests low-risk initial safety-oriented actions.
- Explicitly communicates uncertainty and limitations.

The system does NOT:

- Establish medical diagnoses.
- Replace licensed medical professionals.
- Autonomously prescribe treatment.
- Perform automated triage without human interaction.
- Guarantee clinical outcomes.

---

## 3. Intended User

Primary intended user:

- Non-medically trained individuals (community members, caregivers, isolated operators).

Secondary intended user (supervised deployment phase):

- Healthcare professionals using the system as structured decision support.

---

## 4. Intended Environment

The system is designed for:

- Rural or remote environments.
- Maritime or offshore settings.
- Resource-limited zones.
- Geographic isolation scenarios.
- Situations with delayed emergency response.

Internet connectivity may be available but cannot be assumed for physician interaction.

---

## 5. Operational Boundaries

The system must:

- Explicitly warn when critical input data is missing.
- Block progression when absence of key variables creates unacceptable risk.
- Clearly communicate uncertainty levels.
- Escalate warnings when high-risk patterns are detected.
- Log operational decisions for traceability.

In extreme isolation scenarios (no access to medical assistance by any means), the system may continue to provide structured guidance while explicitly warning that:

- The probability of error increases.
- Clinical deterioration may occur.
- There is risk of death despite guidance.

The system must never imply certainty under uncertainty conditions.

---

## 6. Regulatory Classification Hypothesis (Preliminary)

Argentina (ANMAT):

Likely classification: Medical Device Software (Software as a Medical Device – SaMD).
Risk class to be determined based on:
- Degree of autonomy,
- Clinical impact,
- Intended environment.

Current design aims to remain in a moderate risk category by:

- Avoiding autonomous diagnosis.
- Avoiding therapeutic automation.
- Maintaining human-in-the-loop interaction.

Canada (Health Canada):

Likely classification under Medical Device Regulations (SOR/98-282).
Preliminary hypothesis:
- Class II or Class III depending on claimed functionality.

Final classification requires formal regulatory consultation.

---

## 7. Governance Positioning

This system is designed under the principle of:

- Human responsibility retention.
- Explicit uncertainty modeling.
- Traceable reasoning.
- Safety-first prioritization.
- Non-autonomous clinical authority.

Any feature that introduces autonomous clinical authority must trigger regulatory re-evaluation.

---

## 8. Evolution Roadmap (Regulatory)

Phase 1:
Decision support only.
No autonomous action.
Explicit uncertainty communication.

Phase 2:
Integrated sensor data.
Enhanced risk modeling.
Continued human acknowledgment requirement.

Phase 3 (Conditional):
Regulatory submission pathway in Argentina.
Parallel preparation for Canadian certification.

No clinical deployment shall occur without jurisdiction-specific regulatory clearance.

---

## 9. Legal Disclaimer (Development Phase)

This repository represents a research and development initiative.

It does not constitute a certified medical device.

No real-world patient deployment is authorized under this version.

Clinical validation, regulatory approval, and formal certification are mandatory prior to operational use.
