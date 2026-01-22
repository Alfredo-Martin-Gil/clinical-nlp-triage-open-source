# clinical-nlp-triage-open-source

## Executive Summary

This open-source project explores how **rule-based clinical reasoning and NLP**
can support **early triage decisions under uncertainty** in emergency and prehospital care.

It is grounded in **real-world clinical workflows**, focuses on **safety and explainability**,
and is designed as a **research and educational baseline** — not a medical device.

The project demonstrates how structured rules, red-flag detection, and transparent logic
can help **reduce cognitive overload**, surface potential risks early,
and support clinical judgment in **time-critical, information-poor environments**.

**Relevant for:** clinical decision support, digital health operations,
and safe AI deployment in healthcare (remote-first teams).

---

Open-source prototype of a rule-based and NLP-assisted triage system for emergency and prehospital care.

> ⚠️ **Clinical safety notice**  
> This project is an experimental research/prototype environment.  
> It is **not a medical device**, has **no regulatory approval**, and **must not be used**
> to make decisions about real patients.

---

## 🔎 Related Conceptual Work

This project is part of a broader exploration of **clinical decision-making under uncertainty**
in prehospital care.

A detailed operational description of how real-world decisions are made — without algorithms
or models — is documented here:

👉 **[prehospital-clinical-decision-uncertainty](https://github.com/Alfredo-Martin-Gil/prehospital-clinical-decision-uncertainty)**

That repository provides the clinical reasoning context that informs this implementation,
but contains **no code and no decision automation**.

---

## 🧭 Clinical Origin & Ethical Foundation

This project is grounded in real-world emergency and prehospital clinical practice.

For a detailed explanation of the clinical motivation, problem framing, and ethical positioning behind this initiative, see:

➡️ **[Clinical Origin of the Project](docs/clinical_origin.md)**

This document describes *why* this project exists, the role of uncertainty and cognitive overload in triage, and the principles that guide its development.

---

## Clinical Reasoning and Guideline Alignment

This project follows internationally accepted principles of **risk-based triage**
and early clinical **risk stratification** in emergency and prehospital settings.

### What this project does (and does not) do
- It supports **early risk awareness and prioritization** under uncertainty.
- It does **not** provide diagnoses, replace clinician judgment, or make autonomous decisions.
- Triage priority ≠ diagnosis; decision support ≠ autonomous decision-making.

### Alignment with validated international frameworks
The approach is conceptually aligned with:
- Guideline-based **early risk stratification** (condition-specific, published by international societies).
- International triage systems where **high-risk features override transient stability**, including **ESI**, **CTAS**, and **MTS**.

### Relation to ACLS / advanced life support
ACLS algorithms are not implemented here because they apply to cardiac arrest, life-threatening arrhythmias, or established instability.  
This project operates **upstream of ACLS**, at the triage and early assessment phase, and does not interfere with ALS activation when deterioration occurs.

### Where condition-specific detail lives
Condition-specific guideline notes (e.g., syncope, chest pain, dyspnea, stroke, sepsis, trauma) are maintained under:

`docs/clinical_entities/`

---

## 🧠 Problem Statement

In emergency and prehospital settings, clinical decisions are frequently made under conditions of:

- incomplete or ambiguous information,
- high cognitive load,
- time pressure,
- and, in many contexts, limited or absent access to experienced clinicians.

In these environments, the primary risk is not a lack of medical knowledge, but **decision-making under uncertainty**.

This project originates from real-world clinical practice, where triage often relies on brief, unstructured notes, subjective descriptions, and early symptom narratives that may hide critical red flags.

---

## 🚑 Clinical Context

This project is grounded in real emergency and prehospital medicine workflows, including:

- ambulance and out-of-hospital care,
- emergency department triage,
- low-resource or understaffed settings,
- early patient contact before full diagnostic data is available.

The system is designed to explore how structured rules and NLP techniques can help
**reduce cognitive overload**, surface potential red flags early,
and support — not replace — clinical judgment.

---

## ⚖️ Project Philosophy

### What this project IS
- A research and educational prototype.
- A clinical decision-support exploration tool.
- A transparent, explainable baseline for triage reasoning.
- A multidisciplinary collaboration between clinicians, bioengineers and AI practitioners.

### What this project is NOT
- ❌ Not a medical device.
- ❌ Not a diagnostic system.
- ❌ Not an autonomous decision-maker.
- ❌ Not intended for real patient care.

The goal is to **augment human decision-making**, especially in environments where uncertainty and cognitive overload increase the risk of preventable harm.

---

## 🚑 Overview

This project aims to build a minimal, open-source triage assistant using:

- **Clinical NLP**
- **Rule-based scoring**
- **Red-flag detection**

The system is designed for **multidisciplinary teams**
(clinicians, bioengineers, NLP/ML, data and documentation)
working asynchronously across multiple time zones (LATAM, Europe, North America).

The initial versions focus on:

- Extracting symptoms and red flags from free-text triage notes (Spanish/English).
- Assigning severity weights.
- Producing a simple **priority/urgency score**.
- Documenting all assumptions, limitations and safety risks clearly.

---

## 🧩 Project Structure

```text
clinical-nlp-triage-open-source/
│
├── data/
│   ├── lexicon_redflags.csv
│   └── notes_synthetic.csv
│
├── notebooks/
│   └── triage_rules_baseline.ipynb
│
├── src/
│   └── (future Python modules)
│
├── outputs/
│   └── predictions.csv
│
├── docs/
│   ├── baseline_scoring.md
│   └── roles.md
│
├── README.md
├── CONTRIBUTING.md
└── LICENSE













