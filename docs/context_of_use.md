# Context of Use – v0.1

## 1. Deployment Jurisdiction (Initial)

Primary target for first real-world deployment:
- Argentina

Future expansion considered:
- Canada

This document is written to remain compatible with future certification pathways in both jurisdictions.

---

## 2. Intended Environment

The system is intended for use in environments where there is no immediate access to a physician.

Examples include:
- Rural or remote areas
- Maritime settings (boats, offshore)
- Resource-limited zones
- Locations with geographic isolation
- Areas with delayed emergency response times

Internet connectivity may be available for model access and updates, but the system is designed for scenarios where direct physician interaction is not immediately accessible.

---

## 3. Intended User

Primary intended user:
- Non-medically trained individuals

Examples:
- Community members
- Caregivers
- Individuals assisting a patient in remote locations

Early implementation stages may include supervised pilot usage with medical oversight.

---

## 4. Intended Population

- Adults only (≥18 years)

Pediatric use is explicitly excluded in v0.x and would require a separate validation pathway.

---

## 5. System Objective

The core objective of the system is:

> To provide a survival opportunity to individuals who would otherwise lack technical medical guidance in time-critical situations.

The system aims to detect high-risk clinical signals and escalate appropriately.

---

## 6. Functional Scope (Current Vision)

The system is envisioned as a multimodal decision-support platform that may include:

- Text input (symptom description)
- Voice interaction (patient or assistant)
- Wearable or garment-based sensor interface (future phase)
    - Heart rate
    - Oxygen saturation
    - ECG
    - Digital auscultation
- Visual input (camera/video feed)
    - Remote professional review
    - AI-assisted contextual interpretation (future phase)

Initial versions focus on structured risk escalation logic.

---

## 7. Escalation Philosophy

The system does not replace physicians.

Escalation model (Policy A):
- Intermediate risk → Human contact required
- High risk → Immediate medical attention required
- Low risk → Monitor and seek help if worsening

The system is conservative by design.

---

## 8. Explicit Non-Claims (Critical Safety Boundary)

The system does NOT:

- Provide medical diagnosis
- Prescribe treatment
- Replace professional medical judgment
- Provide medication dosing instructions
- Operate as an autonomous clinical authority

It functions strictly as a risk detection and escalation assistant.

---

## 9. Ethical and Regulatory Direction

Although early development is research-oriented, the architecture is being designed with future certification in mind.

Future alignment targets:
- Software as a Medical Device (SaMD) principles
- Traceability of decisions
- Deterministic risk layers
- Auditability and reproducibility

Governance and regulatory documentation will precede any real-world patient testing.

---

## 10. Development Philosophy

The system is being developed incrementally:

1. Deterministic baseline (current stage)
2. Traceability layer (v0.2 implemented)
3. Architecture separation (future)
4. Validation framework
5. Interface and device integration
6. Supervised field evaluation
7. Formal regulatory pathway

Each phase must be internally coherent and auditable before progression.
