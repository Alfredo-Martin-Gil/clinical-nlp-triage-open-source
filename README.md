# clinical-nlp-triage-open-source

Open-source prototype of a rule-based and NLP-assisted triage system for emergency and prehospital care.

> ⚠️ **Clinical safety notice**  
> This project is an experimental research/prototype environment.  
> It is **not a medical device**, has **no regulatory approval**, and **must not be used** to make decisions about real patients.

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

markdown
Copy code

Copiás todo ese bloque y lo pegás en `README.md` en GitHub (igual que hiciste con `baseline_scoring.md` y `roles.md`), opción **“Commit directly to main”**.

Cuando lo tengas actualizado, ya vas a tener:

- README profesional para compartir con Carina.
- Documentación interna consistente (baseline, roles, contributing).
- Un repo presentable para cualquier colaborador nuevo.
::contentReference[oaicite:0]{index=0}











