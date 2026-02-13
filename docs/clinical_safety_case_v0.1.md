# Clinical Safety Case – v0.1

## 1. Safety Goal

The system is acceptably safe for its intended use as a structured clinical decision support tool in environments without immediate physician access.

The system does not claim diagnostic authority or autonomous treatment capability.

---

## 2. Top-Level Safety Claim

The system reduces risk compared to absence of structured guidance in isolated environments, without introducing unacceptable additional risk.

---

## 3. Supporting Safety Claims

### Claim 1: The system does not introduce autonomous clinical authority.

Evidence:
- Regulatory Positioning Document
- Software Lifecycle Procedure
- Change Control Procedure

---

### Claim 2: The system explicitly models and communicates uncertainty.

Evidence:
- Clinical Uncertainty Document
- Uncertainty Model
- Escalation Behavior Definition

---

### Claim 3: High-severity risks are identified and mitigated.

Evidence:
- Hazard Model
- Risk Management Procedure
- Escalation Triggers
- Blocking Mechanisms

---

### Claim 4: The system prioritizes escalation over reassurance in ambiguous scenarios.

Evidence:
- Risk Governance Principle
- Conservative Framing Rules
- Failure Behavior Contract

---

### Claim 5: Missing critical data triggers warnings or blocking.

Evidence:
- Failure Behavior Contract
- Risk Management Procedure
- Software Lifecycle Procedure

---

## 4. Hazard Mitigation Mapping

Each hazard documented in the Hazard Model must:

- Identify mitigation mechanism
- Reference code implementation
- Reference uncertainty handling
- Reference escalation logic

No hazard may remain unmitigated without explicit residual risk justification.

---

## 5. Residual Risk Justification

Residual risk is considered acceptable when:

- The system provides safer guidance than no structured intervention.
- The system does not overstate certainty.
- The system escalates in high-risk patterns.
- The system clearly communicates limitations.

In extreme isolation scenarios, residual risk may remain high; however, absence of structured guidance presents greater risk.

---

## 6. Human Responsibility Retention

The system:

- Requires human acknowledgment.
- Does not override human judgment.
- Does not claim medical authority.
- Does not guarantee survival.

Responsibility remains human.

---

## 7. Safety Boundary Conditions

The system must not:

- Minimize severe red flags.
- Suppress escalation signals.
- Provide deterministic diagnostic conclusions.
- Continue without warning when critical inputs are missing.

Violation of these boundaries invalidates this safety case.

---

## 8. Ongoing Safety Assurance

Any Major Change requires:

- Hazard model update
- Risk reassessment
- Safety case revision

The safety case is invalid if documentation lags behind implementation.

---

## 9. Certification Pathway Intent

This safety case structure is designed to support:

- ANMAT submission (Argentina)
- Health Canada SaMD review

It follows argument-based safety reasoning aligned with medical device expectations.
