# Change Control Procedure – v0.1

## 1. Purpose

This document defines how changes to the system are evaluated, approved, documented, and implemented.

It ensures:

- Regulatory traceability
- Risk reassessment
- Prevention of uncontrolled scope expansion
- Alignment with ISO 13485 and IEC 62304 expectations

---

## 2. Scope

This procedure applies to changes affecting:

- Intended use
- Clinical behavior
- Risk thresholds
- Escalation logic
- Output structure
- Uncertainty modeling
- Sensor integration
- Regulatory claims

It does not apply to minor editorial corrections without functional impact.

---

## 3. Change Classification

Changes must be classified before implementation.

### Minor Change
- Documentation clarification
- Refactoring without logic modification
- Formatting improvements

### Moderate Change
- New red flag definitions
- Modified scoring logic
- Updated escalation conditions
- UI wording affecting interpretation

### Major Change
- Expansion of intended use
- Introduction of autonomous behavior
- Integration of physiological sensors
- Modification of decision authority
- Expansion to new jurisdiction
- Alteration of regulatory positioning

Major changes require full risk reassessment.

---

## 4. Change Evaluation Process

Before implementation:

1. Describe the change.
2. Classify its level (Minor / Moderate / Major).
3. Identify impacted documents.
4. Evaluate hazard model impact.
5. Evaluate regulatory impact.
6. Determine whether risk reassessment is required.

No code modification may occur before classification.

---

## 5. Risk Reassessment Trigger

Risk reassessment is mandatory if the change:

- Alters escalation logic
- Modifies uncertainty thresholds
- Reduces blocking conditions
- Expands system authority
- Introduces new clinical data sources
- Changes failure behavior contract

---

## 6. Documentation Requirements

Each significant change must:

- Reference impacted QMS documents
- Reference hazard model sections
- Reference regulatory positioning sections
- Include justification for acceptability

Commit messages must reflect:

- Nature of change
- Impact level
- Risk evaluation status

---

## 7. Approval

During pre-certification phase:

- Project lead approval required for Moderate and Major changes.

Future certified phase:

- Formal documented approval workflow required.

---

## 8. Release Governance

A release version must not include:

- Unclassified changes
- Undocumented logic modifications
- Risk-impacting changes without reassessment
- Major changes without explicit justification

---

## 9. Governance Principle

No functional expansion is allowed without explicit documentation.

Uncontrolled expansion invalidates regulatory readiness.

Traceability overrides development speed.
