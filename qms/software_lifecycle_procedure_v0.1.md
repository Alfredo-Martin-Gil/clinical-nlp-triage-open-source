# Software Lifecycle Procedure – v0.1

## 1. Purpose

This document defines the structured software development lifecycle (SDLC) for this project.

It is designed to be structurally compatible with:

- IEC 62304 (Medical Device Software Lifecycle)
- IMDRF SaMD lifecycle expectations
- Health Canada documentation requirements
- ANMAT software device review expectations

This version represents a pre-certification structured framework.

---

## 2. Lifecycle Model

The project follows a controlled iterative lifecycle with the following phases:

1. Requirement Definition  
2. Risk Assessment  
3. Architectural Design  
4. Implementation  
5. Verification  
6. Documentation Update  
7. Release Decision  

No phase may be skipped.

---

## 3. Requirements Definition

All new features must:

- Be documented before implementation.
- Define intended behavior.
- Define limitations.
- Reference regulatory positioning.
- Reference hazard analysis impact.

Requirements must reside in `/docs/` or `/qms/` before code is merged.

---

## 4. Risk Pre-Implementation Check

Before implementation:

- Hazard model must be reviewed.
- Risk impact must be evaluated.
- Escalation logic impact must be documented.
- Uncertainty modeling impact must be reviewed.

No new feature may expand clinical authority without risk reassessment.

---

## 5. Architectural Design

For any functional expansion:

- Design intent must be documented.
- Input/output boundaries must be defined.
- Escalation behavior must be described.
- Failure handling must be specified.

Design must align with:
- Risk Management Procedure
- Regulatory Positioning
- Clinical Uncertainty Model

---

## 6. Implementation Controls

All code changes must:

- Be version controlled.
- Be accompanied by clear commit messages.
- Avoid undocumented logic changes.
- Maintain traceability to documented requirement.

No undocumented clinical logic modification is permitted.

---

## 7. Verification

Verification must include:

- Baseline smoke testing
- Contract tests (output schema)
- Escalation trigger validation
- Negative case validation
- Uncertainty behavior validation

Verification must confirm:

- No unintended autonomy introduced
- No silent escalation suppression
- No ambiguity introduced in risk communication

---

## 8. Release Criteria

A version may be considered releasable (development phase) only if:

- Risk assessment updated
- Documentation aligned
- Tests passing
- No open high-severity hazards
- Regulatory positioning unchanged or reviewed

---

## 9. Change Classification

Changes must be classified as:

Minor:
- Documentation clarification
- Refactoring without logic impact

Moderate:
- New red flags
- Modified scoring thresholds
- Interface adjustments

Major:
- Change in intended use
- Expansion of autonomy
- Sensor integration
- Altered escalation authority

Major changes require full risk reassessment.

---

## 10. Post-Change Review

After merging significant changes:

- Hazard model must be reviewed.
- Risk residual assessment must be confirmed.
- Documentation cross-links must be verified.

No silent expansion of authority is allowed.

---

## 11. Lifecycle Governance Principle

The system must evolve conservatively.

Speed of iteration must never exceed:

- Risk documentation capacity
- Governance update capacity
- Verification capacity

If documentation lags behind implementation, development must pause.
