# Document Control Procedure – v0.1

## 1. Purpose

This procedure defines how controlled documents are created, modified, versioned, and archived within this project.

It ensures:

- Traceability
- Version integrity
- Change accountability
- Regulatory compatibility

---

## 2. Scope

This procedure applies to:

- QMS documents
- Regulatory positioning documents
- Risk documentation
- Hazard models
- Clinical positioning documents
- Safety contracts
- Software lifecycle documentation

It does NOT apply to exploratory notes or non-controlled drafts.

---

## 3. Controlled Documents

A document is considered "controlled" if it:

- Defines intended use
- Defines regulatory positioning
- Defines safety constraints
- Defines risk handling
- Defines system boundaries
- Influences clinical behavior

Controlled documents must reside in:

- `/qms/`
- `/docs/`

---

## 4. Versioning Rules

Each controlled document must:

- Include version number (v0.x for pre-certification phase)
- Be updated only via Git commit
- Maintain clear commit messages
- Avoid silent modifications

Major version change:
- Change in intended use
- Change in risk posture
- Change in autonomy scope

Minor version change:
- Clarification
- Wording refinement
- Structural improvement

---

## 5. Change Authorization

During pre-certification phase:

- Project lead approval is required for:
  - Intended use changes
  - Risk classification changes
  - Operational boundary changes
  - Autonomy expansion

Future phase:
- Formal signature and approval workflow required.

---

## 6. Traceability Requirements

Any modification affecting:

- Risk logic
- Escalation behavior
- Uncertainty thresholds
- Output structure

must reference:

- Relevant hazard model section
- Relevant uncertainty section
- Relevant regulatory positioning section

Cross-document traceability is mandatory.

---

## 7. Archiving Policy

Superseded documents:

- Must not be deleted.
- Must remain in version history.
- May be marked as "superseded".

No historical risk documentation may be erased.

---

## 8. Repository Integrity

Direct modification of controlled documents outside version control is prohibited.

All changes must:

- Be committed
- Include explicit message
- Maintain auditability

---

## 9. Compliance Objective

This procedure is designed to align with:

- ISO 13485 documentation control principles
- ISO 14971 traceability expectations
- IMDRF SaMD documentation structure
- Health Canada documentation expectations
- ANMAT traceability requirements

It becomes active immediately upon publication.
