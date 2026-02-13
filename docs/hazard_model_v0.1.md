# Hazard Model – v0.1

## 1. Scope

This document identifies potential hazards associated with the system described in `context_of_use.md`.

The system is intended for adult patients in remote or medically underserved environments, used by non-medically trained individuals.

The purpose of this model is to identify life-threatening failure modes early in development.

---

## 2. Worst-Case Harm

Worst credible harm:

> Delayed or absent escalation of a life-threatening condition resulting in preventable death.

All system risks are evaluated against this outcome.

---

## 3. Primary Hazard Categories

### H1 – False Negative (Missed Critical Condition)

Description:
- The system fails to detect a high-risk condition.

Examples:
- Undetected cardiac event
- Undetected severe hypoxia
- Undetected hemorrhage

Potential Harm:
- Delay in emergency escalation
- Increased mortality

Mitigation Strategy (v0.x):
- Conservative escalation policy (intermediate/high → human contact)
- Deterministic baseline logic
- Traceability of decisions
- Future redundancy in sensor + symptom channels

---

### H2 – False Positive (Over-escalation)

Description:
- The system escalates non-critical cases.

Potential Harm:
- Resource misuse
- Panic
- System distrust

Severity:
- Low compared to H1
- Acceptable bias toward safety in early stages

Mitigation:
- Conservative messaging
- Clear explanation layer
- Human override always allowed

---

### H3 – Incorrect Recommendation

Description:
- The system outputs misleading action guidance.

Examples:
- Recommends monitoring when urgent care is needed
- Provides ambiguous language

Mitigation:
- Strict non-diagnostic positioning
- Escalation-based output only
- No treatment or dosing advice

---

### H4 – Technical Failure

Description:
- Crash
- Network failure
- Partial sensor malfunction
- Data corruption

Potential Harm:
- Loss of guidance in critical moment

Mitigation:
- Fail-safe messaging
- Offline fallback (future phase)
- Clear “system unavailable” state
- No silent failure

---

### H5 – Sensor Misinterpretation (Future Device Phase)

Description:
- Incorrect heart rate detection
- False SpO2 reading
- Noise interpreted as signal
- Visual misclassification

Potential Harm:
- False reassurance
- False alarm

Mitigation (future):
- Multi-signal redundancy
- Confidence scoring
- Sensor validation layer
- Explicit uncertainty display

---

### H6 – User Misuse

Description:
- Incorrect device placement
- Incomplete answers
- Language misunderstanding

Potential Harm:
- Garbage-in → incorrect escalation

Mitigation:
- Guided interaction
- Voice clarification
- Instruction layer
- Future usability validation studies

---

## 4. Risk Philosophy

The system prioritizes:

- Avoiding false negatives over false positives
- Escalation over reassurance
- Determinism over opaque inference (early phases)
- Auditability over performance

---

## 5. Development Constraints

No real-world deployment is permitted until:

- Hazard mitigation strategies are documented
- Supervised validation phase completed
- Governance framework established
- Legal review conducted

---

## 6. Next Phase

The next development phase must integrate:

- Hazard-to-feature traceability
- Explicit failure state behavior
- Escalation audit logging
- Sensor validation protocols (future hardware phase)
