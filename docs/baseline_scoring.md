# Baseline Scoring

This document describes the current baseline scoring logic implemented in the notebook:

`notebooks/triage_rules_baseline.ipynb`

The baseline is intentionally simple, transparent, and fully rule-based.

---

## 1. Purpose

Provide an interpretable first-pass triage risk signal from free-text notes by:

- Detecting red-flag clinical terms
- Applying severity weights
- Handling simple negation
- Handling simple historical context
- Producing a numeric score and mapped risk label

This is a research and educational baseline, not a medical device.

---

## 2. Lexicon Structure

`data/lexicon_redflags.csv`

Columns:

- term → phrase to match
- category → clinical entity
- weight → integer severity weight (1–5)
- language → language code
- note → human explanation

Example:

exertional syncope,syncope,5,en,Exertional syncope

---

## 3. Matching Logic

For each note:

- Convert text to lowercase
- For each lexicon term:
  - Check if term appears as substring

If term appears → candidate match.

---

## 4. Negation Handling (Simple Heuristic)

Before accepting a match, the system checks a small window of text before the term for negation cues such as:

- no
- denies
- without
- not

If a negation cue is found close before the term:

→ The match is discarded.

Goal: avoid counting statements like:

"No chest pain"

This is not full syntactic negation detection.

---

## 5. Historical / Past Context Handling (Simple Heuristic)

If the text contains historical cues such as:

- history of
- previous
- years ago
- prior

Then matched term weight is reduced (downweighted).

Goal: distinguish active complaint vs past history.

Example:

"History of chest pain years ago"  
Counts with reduced weight.

---

## 6. Score Computation

For each accepted match:

- Add its weight to total score

Total score = sum(weight_i)

The system also keeps a list of matched terms for debugging.

---

## 7. Score → Label Mapping

Current thresholds:

- score >= 5 → high
- score 3–4 → intermediate
- score <= 2 → low

These thresholds are heuristic and expected to evolve.

---

## 8. Output Fields

Notebook produces:

- predicted_label
- score
- matched_terms

Exported to:

`outputs/predictions.csv`

---

## 9. Design Principles

- Deterministic
- Transparent
- Auditable
- No machine learning
- No embeddings
- No hidden state

This baseline exists to:

Establish a measurable, explainable reference point before introducing more complex NLP techniques.

---

## 10. Known Limitations

- Substring matching only
- No tokenization
- No lemmatization
- No spelling tolerance
- Very simple negation handling
- Very simple temporal handling

These limitations are intentional at this stage.
