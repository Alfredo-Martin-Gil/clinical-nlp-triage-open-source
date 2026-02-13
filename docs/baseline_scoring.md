# Baseline Scoring (v0.1)

This document describes the **current v0.1 baseline** implemented in code under:

- `src/triage/engine.py` (core)
- `src/rules_engine.py` (CLI)

The v0.1 baseline is intentionally simple, transparent, deterministic, and designed for:

- **non-clinical users**
- **risk escalation**
- **human contact required** for **intermediate/high** risk

> ⚠️ Clinical safety notice  
> This is a research/prototype baseline. It does not diagnose or treat.  
> Do not use it as a substitute for professional medical judgment.

---

## 1. Purpose

Provide an interpretable **risk escalation signal** from free-text notes by:

- Detecting red-flag terms (substring matching)
- Counting detected red flags (hits)
- Mapping hits to a coarse risk level
- Producing safe, conservative recommended actions

---

## 2. Inputs

### Notes
Expected column:

- `triage_note`

### Lexicon
Expected column:

- `term`

---

## 3. Matching Logic (v0.1)

For each note:

- Convert text to lowercase
- For each lexicon term:
  - Check if term appears as substring
- Collect matched terms (traceable output)

---

## 4. Score Computation (v0.1)

- `risk_score` = number of matched terms (hits)

---

## 5. Score → Risk Level Mapping (v0.1)

- hits >= 2 → `high`
- hits == 1 → `intermediate`
- hits == 0 → `low`

---

## 6. Escalation Policy (Non-clinical users)

- `intermediate` or `high` → **requires_human_contact = true**
- `low` → **requires_human_contact = false**

Recommended actions are conservative and escalation-oriented.

---

## 7. Output Contract (v0.1)

The baseline produces:

- `engine_version`
- `risk_level`
- `risk_score`
- `detected_red_flags` (pipe-separated terms)
- `requires_human_contact`
- `recommended_action`
- `safety_notice`

---

## 8. Roadmap Note

More advanced features (weights, negation handling, temporal/history heuristics, matched term metadata)
will be introduced in later versions (v0.2+), with tests and metric protocols.

Notebooks remain exploratory and must not be treated as the authoritative baseline.
