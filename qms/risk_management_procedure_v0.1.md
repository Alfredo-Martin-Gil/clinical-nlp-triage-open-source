# Risk Management Procedure – v0.1

## 1. Purpose

This procedure defines the structured approach to risk management for the system described in this repository.

It is designed to be structurally compatible with:

- ISO 14971 (Risk Management for Medical Devices)
- IMDRF SaMD risk framework
- Health Canada expectations
- ANMAT medical device risk documentation requirements

---

## 2. Scope

This procedure applies to:

- Software logic
- Clinical decision support outputs
- Escalation behavior
- Uncertainty handling
- Sensor integration (future phases)
- Human–AI interaction boundaries

---

## 3. Risk Management Process

The risk management lifecycle includes:

1. Hazard Identification  
2. Risk Analysis  
3. Risk Evaluation  
4. Risk Control Implementation  
5. Residual Risk Assessment  
6. Post-change Review

This process must be repeated for each major system modification.

---

## 4. Hazard Identification

Hazards may arise from:

- Incorrect risk classification
- Missed escalation triggers
- False reassurance
- Ambiguous uncertainty communication
- Incomplete data processing
- Overconfidence signaling
- Sensor misinterpretation (future phases)
- Interface misuse

All hazards must be documented in:

- `/docs/hazard_model_vX.md`

---

## 5. Risk Analysis

Each identified hazard must include:

- Hazard description
- Foreseeable sequence of events
- Potential clinical harm
- Severity classification
- Probability estimation (qualitative during early phase)

---

## 6. Risk Evaluation Criteria

Risk acceptability must consider:

- Potential for death
- Potential for serious injury
- Probability of occurrence
- Detectability
- Mitigation feasibility

High-severity risks require explicit mitigation documentation.

---

## 7. Risk Control Measures

Risk controls may include:

- Blocking unsafe progression
- Mandatory warnings
- Explicit uncertainty communication
- Escalation triggers
- Conservative output framing
- Human acknowledgment requirement
- Restricting autonomous behaviors

All implemented controls must be traceable to:

- Specific hazard entries
- Specific code modules
- Specific documentation sections

---

## 8. Residual Risk

Residual risk must be:

- Explicitly acknowledged
- Documented
- Justified as acceptable under defined intended use

Residual risk must never be implicitly ignored.

---

## 9. Change-Driven Risk Reassessment

Any change affecting:

- Intended use
- Risk classification
- Escalation logic
- Output authority
- Sensor integration

must trigger:

- Risk reanalysis
- Hazard model update
- Documentation revision

No functional expansion is permitted without risk reassessment.

---

## 10. Risk Governance Principle

The system must default to:

- Conservative decision framing
- Explicit uncertainty acknowledgment
- Escalation over reassurance
- Human responsibility retention

The system must never:

- Claim certainty under uncertainty
- Imply diagnostic authority
- Minimize high-severity risk signals

---

## 11. Integration With Repository Artifacts

This procedure is directly linked to:

- `docs/hazard_model_vX.md`
- `docs/failure_behavior_contract_vX.md`
- `docs/uncertainty_model_vX.md`
- `docs/regulatory_positioning_v0.1.md`

Traceability between these documents is mandatory.
