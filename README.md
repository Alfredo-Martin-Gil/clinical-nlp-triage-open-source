# clinical-nlp-triage-open-source

Open-source prototype of a rule-based and NLP-assisted triage system for emergency and prehospital care.

> ⚠️ **Clinical safety notice**  
> This project is an experimental research/prototype environment.  
> It is **not a medical device**, has **no regulatory approval**, and **must not be used** to make decisions about real patients.

## 🧭 Clinical Origin & Ethical Foundation

This project is grounded in real-world emergency and prehospital clinical practice.

For a detailed explanation of the clinical motivation, problem framing, and ethical positioning behind this initiative, see:

➡️ **[Clinical Origin of the Project](docs/clinical_origin.md)**

This document describes *why* this project exists, the role of uncertainty and cognitive overload in triage, and the principles that guide its development.

## Clinical Reasoning and Guideline Alignment

This project is grounded in internationally accepted principles of clinical risk stratification and triage.  
It does **not** aim to diagnose conditions or replace clinician judgment, but to support **early risk awareness and prioritization** in emergency and prehospital settings.

### Scope and methodological positioning
The triage logic implemented and evaluated in this project focuses on:
- Early identification of **high-risk clinical features**
- Reduction of **cognitive load** under time pressure
- Support for **decision-making in uncertain contexts**, particularly in prehospital or low-resource environments

This approach deliberately precedes definitive diagnosis or advanced treatment algorithms.

---

### Alignment with international clinical guidelines

The clinical reasoning underlying this project is conceptually aligned with the following validated international guidelines and frameworks:

#### Syncope and transient loss of consciousness
- **European Society of Cardiology (ESC)**  
  *2018 ESC Guidelines for the diagnosis and management of syncope*  
  These guidelines emphasize early risk stratification based on age, prodromal features, comorbidities, and clinical context.  
  High-risk features warrant urgent evaluation even in initially stable patients.

- **American College of Emergency Physicians (ACEP)**  
  *Clinical Policy for the Evaluation of Syncope in the Emergency Department*  
  ACEP highlights the importance of prioritizing sensitivity over specificity during initial assessment, recognizing that short-term stability does not exclude serious underlying pathology.

- **Canadian Syncope Risk Score (CSRS)**  
  While not implemented as a rigid scoring system, the project follows the same conceptual framework:
  age, clinical context, risk factors, and presentation guide triage priority rather than definitive diagnosis.

- **NICE Guidelines (UK)**  
  *Transient loss of consciousness (TLoC)*  
  NICE guidance reinforces that early triage decisions should identify patients who cannot be safely managed without urgent in-hospital assessment.

---

### Relation to ACLS and advanced life support algorithms
Advanced Cardiac Life Support (ACLS) algorithms are **not directly applied** within this project, as ACLS is designed for the management of:
- Cardiac arrest
- Life-threatening arrhythmias
- Established hemodynamic instability

This project operates **upstream of ACLS**, at the triage and early assessment phase.  
Importantly, it does not delay or interfere with ACLS activation when clinical deterioration occurs.

---

### Triage frameworks and urgency classification
The prioritization logic is consistent with internationally used triage systems, including:
- **Emergency Severity Index (ESI)**
- **Canadian Triage and Acuity Scale (CTAS)**
- **Manchester Triage System (MTS)**

In these systems, the presence of high-risk features overrides transient stability and justifies elevated priority levels.

---

### Ethical and clinical principles
- Triage priority ≠ diagnosis  
- Decision support ≠ autonomous decision-making  
- Final responsibility always remains with a qualified healthcare professional

The system is designed to reduce avoidable harm by supporting clinicians during early, high-uncertainty phases of care.


## 🧠 Problem Statement

In emergency and prehospital settings, clinical decisions are frequently made under conditions of:

- incomplete or ambiguous information,
- high cognitive load,
- time pressure,
- and, in many contexts, limited or absent access to experienced clinicians.

In these environments, the primary risk is not a lack of medical knowledge, but **decision-making under uncertainty**.

This project originates from real-world clinical practice, where triage often relies on brief, unstructured notes, subjective descriptions, and early symptom narratives that may hide critical red flags.

## 🚑 Clinical Context

This project is grounded in real emergency and prehospital medicine workflows, including:

- ambulance and out-of-hospital care,
- emergency department triage,
- low-resource or understaffed settings,
- early patient contact before full diagnostic data is available.

The system is designed to explore how structured rules and NLP techniques can help **reduce cognitive overload**, surface potential red flags early, and support — not replace — clinical judgment.

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

The system is designed for **multidisciplinary teams** (clinicians, bioengineers, NLP/ML, data and documentation) working asynchronously across multiple time zones (LATAM, Europe, North America).

The initial versions focus on:

- Extracting symptoms and red flags from free-text triage notes (Spanish/English).
- Assigning severity weights.
- Producing a simple **priority/urgency score**.
- Documenting all assumptions, limitations and safety risks clearly.

---

## 🧩 Project Structure

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
```




🎯 Goals (v0.1-alpha)
v0.1-alpha is focused on a simple but fully documented baseline:

Define a clinical red-flag lexicon.

Build a synthetic dataset of triage notes (no real patients).

Implement a rule-based baseline scoring model.

Generate baseline predictions (outputs/predictions.csv).

Document the baseline in detail (docs/baseline_scoring.md).

Define the team roles and contribution workflow for future versions.

For the detailed rationale, metrics and limitations of the baseline, see:

docs/baseline_scoring.md

📚 Red-Flag Lexicon
The file data/lexicon_redflags.csv contains terms that represent clinical “red flags” for triage.

Example schema:

term	category	weight	language	note
dolor torácico opresivo	chest_pain	4	es	Suggestive of possible ACS

term: expression to detect in free text

category: clinical cluster (e.g. chest_pain, dyspnea, neuro, sepsis)

weight: contribution to the triage score

language: es or en (initially)

note: brief clinical rationale

The baseline uses a lexicon-based approach, not a trained model.

🧪 Synthetic Dataset
data/notes_synthetic.csv contains synthetic triage notes, generated to:

Avoid any real PHI.

Simulate realistic emergency / prehospital scenarios.

Provide a playground for NLP and rule-based experiments.

Columns include (may evolve):

id

text (triage note)

label_redflag (optional, for evaluation/experiments)

All entries are synthetic and do not represent real patient data.

⚙️ Baseline Logic
The baseline is implemented in:

notebooks/triage_rules_baseline.ipynb

Documented in docs/baseline_scoring.md

Core steps:

Load lexicon_redflags.csv

Load notes_synthetic.csv

Normalize and tokenize triage notes

Detect red-flag terms from the lexicon

Aggregate weights and assign a basic urgency flag

Export predictions to outputs/predictions.csv

Compute basic metrics (precision, recall, F1) for reference

🔎 The baseline is intentionally simple and not clinically safe.
Its main purpose is to provide a reference point to improve upon (v0.1.1, v0.2, etc.).

For a deeper technical description, including metrics and limitations:

docs/baseline_scoring.md

👥 Team & Roles (Multidisciplinary)
This project is designed for multidisciplinary collaboration.
Roles are described in detail in:

docs/roles.md

Key roles include (summary):

Project Lead – overall vision, clinical + AI in healthcare.

Clinical Lead(s) – red-flag criteria, clinical validation, safety.

Bioengineer Lead – bridge between physiology, devices, data structure and technical design.

NLP / ML Lead – models, embeddings, negation handling, evaluation.

Data Engineer / MLOps – reproducibility, environments, pipelines.

Contributors (clinical, bioengineering, NLP/ML, documentation) – incremental improvements, testing, data and docs.

This structure is meant to support:

Asynchronous work across time zones.

Clear responsibility boundaries.

Explicit handling of clinical + bioengineering risks.

🤝 How to Contribute
We welcome contributions from:

Clinicians (EM, internal medicine, primary care, etc.)

Bioengineers / biomedical engineers

NLP & ML practitioners

Data engineers

Documentation & communication contributors

Students who want to learn by doing

Please read:

CONTRIBUTING.md

docs/roles.md

before starting.

Typical contribution paths:

Improve or review the red-flag lexicon.

Extend / refine the synthetic dataset.

Enhance the baseline (e.g. negation handling, preprocessing).

Design new experiments (embeddings, transformers, rule+ML hybrids).

Improve documentation and onboarding for new contributors.

🛡️ Safety, Ethics & Limitations
This project explicitly acknowledges that:

The baseline is not adequate for clinical use.

There is a high risk of:

under-detection (missed red flags),

over-triage (false alarms),

misinterpretation of symptoms.

Therefore:

All experiments are for research and educational purposes only.

Any potential future clinical applications would require:

robust validation,

appropriate regulatory frameworks,

and independent clinical governance.

Safety and explainability are treated as first-class concerns, not add-ons.

🚀 Roadmap (High-Level)
v0.1-alpha (current)
✅ Red-flag lexicon (initial version)

✅ Synthetic triage dataset

✅ Rule-based baseline (lexicon-based)

✅ Baseline documentation (docs/baseline_scoring.md)

✅ Team roles (docs/roles.md)

✅ Contribution guide (CONTRIBUTING.md)

v0.1.1
Negation handling module (e.g. simple NegEx-style rules)

Improved lexicon curation (clinical + bioengineering review)

Cleaner evaluation pipeline (per-category metrics)

v0.2
Hybrid approach: rules + embeddings (e.g. ClinicalBERT / multilingual models)

Richer synthetic datasets (more scenarios, noise, informal language)

Initial API or minimal service layer for demo (non-clinical)

v0.3+
More robust ML models (triage suggestions, not decisions).

Better explainability (why a case is flagged).

Possible dashboards or visualizations for research, not clinical use.

Roadmap may evolve as contributions and team availability change.

🧪 Running the Baseline (Quick Start)
Clone the repository

bash
Copy code
git clone https://github.com/<your-user>/clinical-nlp-triage-open-source.git
cd clinical-nlp-triage-open-source
Create environment & install dependencies (example)

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

pip install -r requirements.txt
Run the notebook

Open notebooks/triage_rules_baseline.ipynb in Jupyter or Google Colab.

Execute all cells.

Check outputs/predictions.csv.

Review the baseline documentation

docs/baseline_scoring.md

👨‍⚕️ Project Lead
Emergency & Prehospital Medicine

Dialysis Physician

MSc in Artificial Intelligence Applied to Healthcare

Focus on safe, explainable and clinically grounded AI in health.

📜 License
This project is released under the terms of the license in:

LICENSE

Please review it before reusing or redistributing the code or datasets.












