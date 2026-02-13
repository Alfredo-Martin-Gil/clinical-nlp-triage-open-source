# Uncertainty Model – v0.1

## 0. Relationship to Clinical Uncertainty (Repository Positioning)

This document defines the **operational** uncertainty model used by the system (thresholds, blocking behavior, and user warnings).

It **implements** the repository’s conceptual positioning described in:
- `docs/clinical_uncertainty.md`

In short:
- `clinical_uncertainty.md` explains *why uncertainty is the default state in real clinical work*.
- This document defines *what the system does when uncertainty is high*.

---

## 1. Purpose

This document defines how uncertainty is modeled, quantified, and handled within the system.

Given the intended use in remote and medically isolated environments, unmanaged uncertainty represents a direct mortality risk.

---

## 2. Core Principle

> High uncertainty must never be silently converted into reassurance.

Uncertainty is considered a first-class variable in decision-making.

---

## 3. Sources of Uncertainty

Uncertainty may arise from:

- Missing sensor signals
- Conflicting physiological inputs
- Incomplete symptom reporting
- Data corruption
- AI service degradation
- Environmental constraints
- User misuse

---

## 4. Uncertainty Categories

### U1 – Low Uncertainty
- Complete data
- Consistent signals
- Deterministic match

System behavior:
- Proceed with normal escalation logic

---

### U2 – Moderate Uncertainty
- Minor missing data
- Limited signal noise
- Partial symptom input

System behavior:
- Escalation bias increased
- Uncertainty visibly displayed
- Decision allowed

---

### U3 – High Uncertainty (Critical Threshold)

Triggers:
- Major missing physiological signals
- Conflicting critical indicators
- Sensor reliability compromised
- AI fallback engaged during critical evaluation
- Incomplete triage in high-risk scenario

System behavior:
- Automatic decision blocked
- Clear warning displayed:

  "System uncertainty is critically high.
   Continuing may result in incorrect guidance.
   Incorrect guidance in this context may contribute to death."

- User must explicitly confirm continuation.
- If medical assistance is available → escalate immediately.
- If no assistance is available → allow guarded continuation with explicit degraded-state flag.

---

## 5. Uncertainty Handling Policy

- Uncertainty cannot reduce risk level.
- Missing data increases uncertainty weight.
- Uncertainty does not auto-downgrade escalation.
- Uncertainty must be logged in decision trace.

---

## 6. Future Implementation Requirements

- Introduce explicit `uncertainty_score`
- Introduce `uncertainty_level` (Low / Moderate / High)
- Integrate uncertainty with failure behavior contract
- Log uncertainty drivers in trace layer

---

## 7. Ethical Constraint

The system must never:

- Hide uncertainty
- Convert uncertainty into normal classification
- Present probabilistic output as deterministic certainty

---

## 8. Development Constraint

No multimodal integration (wearables, video AI, external LLM) may occur
without uncertainty modeling integrated into the decision engine.
