# Failure Behavior Contract – v0.1

## 1. Scope

This document defines how the system behaves under failure conditions.

Given the intended use in remote and resource-limited environments, silent failure is considered unacceptable.

Failure behavior must always be explicit and visible to the user.

---

## 2. Failure Philosophy

The system follows an adaptive failure policy based on environmental constraints.

Primary principle:

> The system must never fail silently.
> The system must never imply safety if uncertainty is high.

Failure response depends on availability of external medical assistance.

---

## 3. Failure Context Categories

### F1 – External Medical Access Available

If external medical support is accessible (even with delay):

System behavior:
- Immediately escalate.
- Display: "System integrity compromised. Seek medical assistance immediately."
- Stop automated risk scoring.

Rationale:
When assistance is possible, conservative escalation minimizes harm.

---

### F2 – No Medical Access Available (Isolated Environment)

Examples:
- Maritime vessel
- Remote expedition
- Rural area without reachable services

System behavior:
- Explicitly inform user that system reliability is degraded.
- Continue processing with available data.
- Display high uncertainty warning:
  "Limited system reliability. Recommendations may be incomplete."

- Escalation bias increases.
- Risk level cannot downgrade due to missing signals.
- Missing data increases uncertainty weighting.

Rationale:
In total isolation, partial guidance may be preferable to none,
but only with explicit risk disclosure.

---

## 4. Technical Failure Types

### T1 – Sensor Failure

- Sensor signal out of range
- Signal unavailable
- Sensor disconnected

Behavior:
- Flag specific sensor as unreliable
- Exclude from confidence weighting
- Increase overall uncertainty
- Never assume normal value

---

### T2 – AI Service Failure (Future Cloud Model)

- Timeout
- Model unreachable
- API error

Behavior:
- Fallback to deterministic core engine
- Notify user of reduced capability
- Log failure event

---

### T3 – Data Corruption

- Malformed input
- Inconsistent timestamps
- Impossible values (e.g., HR = 0 while conscious)

Behavior:
- Reject corrupted values
- Flag inconsistency
- Trigger conservative escalation if ambiguity persists

---

## 5. Uncertainty Handling

The system must make uncertainty visible.

Uncertainty sources:
- Missing data
- Conflicting signals
- Sensor noise
- Partial processing

Future requirement:
- Introduce explicit confidence score
- Display confidence tier (High / Moderate / Low)

---

## 6. Prohibited Behavior

The system must never:

- Auto-downgrade risk due to missing signals
- Suppress warnings
- Hide degraded state
- Present normality assumptions

---

## 7. Development Constraint

No hardware integration or multimodal AI integration is permitted
until failure behavior is defined and tested in simulation.

Failure logic must be implemented before advanced features.
