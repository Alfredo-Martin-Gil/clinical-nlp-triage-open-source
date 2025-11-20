# clinical-nlp-triage-open-source
Open-source prototype of a rule-based and NLP-assisted triage system for emergency and prehospital care.

---

## 🚑 Overview
This project aims to build a minimal, open-source triage assistant using **Clinical NLP**, **rule-based scoring**, and **red-flag detection**.  
It is designed for multidisciplinary teams working asynchronously across multiple time zones (LATAM, North America, Europe).

The initial version focuses on extracting symptoms from free-text triage notes (Spanish/English), assigning severity weights, and producing a priority score.

---

## 🧩 Project Structure
clinical-nlp-triage-open-source/
│
├── data/
│ ├── lexicon_redflags.csv
│ ├── notes_synthetic.csv
│
├── notebooks/
│ └── triage_rules_baseline.ipynb
│
├── src/
│ └── (future Python modules)
│
├── outputs/
│ └── predictions.csv
│
├── docs/
│ └── clinical_guidelines.md
│
├── README.md
└── LICENSE

---

## 🎯 Goals (v0.1 Alpha)
- Define a **clinical lexicon** of red-flag symptoms.  
- Build a synthetic dataset of triage notes.  
- Implement a **baseline scoring model**.  
- Generate predictions and export them to CSV.  
- Document clinical criteria and decision rules.  

---

## 📚 Lexicon (red flags)
The file `data/lexicon_redflags.csv` contains:

| term | category | weight | language | note |
|------|----------|---------|----------|------|
| "dolor torácico opresivo" | chest_pain | 4 | es | Suggestive of ACS |

Weights define the contribution of each symptom to the triage score.

---

## 🧪 Synthetic Dataset
`notes_synthetic.csv` includes:
- patient ID  
- chief complaint  
- free-text triage note  
- demo label (urgent / non-urgent)  
- main category  

All entries are synthetic and do **not** represent real patient data.

---

## ⚙️ Baseline Logic
Located in:  
`notebooks/triage_rules_baseline.ipynb`

Steps:
1. Load lexicon  
2. Parse triage notes  
3. Detect symptoms  
4. Sum category weights  
5. Generate urgency flag  
6. Export predictions  

---

## 🤝 Collaboration Workflow
### Branching
- `main`: stable  
- `dev`: active development  
- Feature branches for specific tasks  

### Issues
Use GitHub Issues to coordinate tasks:
- Clinical validation  
- NLP improvements  
- Lexicon expansion  
- Dataset generation  
- Scoring adjustments  

### Project Board
Kanban board (GitHub Projects):  
**To Do → In Progress → Review → Done**

---

## 🛡️ Privacy Notice
No real patient data is used.  
All datasets are synthetic and anonymized by design.

---

## 🌍 Team Collaboration (Global)
Recommended stack:
- **GitHub** → code, issues, tasks  
- **Google Colab** → collaborative notebooks  
- **Notion** → documentation  
- **Discord/Slack** → communication  

Supports contributors from EU, LATAM, US, and Canada.

---

## 🚀 Roadmap
### v0.1  
- Lexicon  
- Synthetic notes  
- Rule-based scoring  
- First predictions  

### v0.2  
- Negation handling (NegEx)  
- Synonyms / lemmatization  
- Category-level thresholds  

### v0.3  
- Hybrid ML model  
- API (FastAPI)  
- Basic dashboard  

---

## 👨‍⚕️ Project Lead
Emergency & Prehospital Medicine  
Dialysis Physician  
MSc Artificial Intelligence Applied to Healthcare  
