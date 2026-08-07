# Research Context and Prohibited Use — v0.1

## Current context

The current artifact is a repository-based research and educational prototype
executed on synthetic English-language text. It is intended for:

- software behaviour inspection;
- synthetic error analysis;
- clinical knowledge-structuring research;
- evaluation-method design;
- discussion of traceability, human oversight, and governance boundaries.

There is no authorized clinical deployment jurisdiction, healthcare setting,
intended patient population, or patient-facing user group for v0.x.

## Prohibited use

The prototype must not be used to:

- assess or triage a real patient;
- diagnose, exclude, or estimate the probability of disease;
- reassure a patient or caregiver;
- recommend treatment, medication, transport, or disposition;
- replace emergency services, local protocols, medical direction, or clinical
  judgement;
- support unsupervised use by non-medically trained individuals;
- operate in rural, remote, maritime, offshore, ambulance, emergency-department,
  hospital, or home-care workflows;
- process identifiable or real patient data;
- claim deployment, clinical validation, or regulatory status.

## Current users

Current users are limited to reviewers examining the repository for research,
education, software testing, or portfolio assessment. Generated outputs are
experimental artifacts and must not be acted upon clinically.

## Current data boundary

- Data type: synthetic text created for this repository.
- Language: English in the current dataset and lexicon.
- Population: no validated patient population; labels are project-assigned
  synthetic reference categories.
- Privacy: absence of patient data does not remove the need for future privacy,
  ethics, and data-governance review.

## Current functional boundary

The engine performs lowercase substring matching, hit counting, internal band
assignment, and trace-field generation. It does not implement:

- weighted scoring;
- negation or temporal interpretation;
- diagnostic reasoning;
- clinically validated escalation;
- uncertainty blocking;
- sensor, voice, image, wearable, ECG, oximetry, or auscultation input;
- remote professional review;
- a patient-facing interface.

## Future context-of-use work

Rural, remote, prehospital, professional, or patient-facing contexts remain
research questions only. They must not be selected as an intended use until a
future version has:

1. a clearly defined problem, user, environment, population, and workflow;
2. clinical, human-factors, privacy, security, ethics, and regulatory review;
3. verified requirements and hazard controls;
4. a justified reference standard and evaluation protocol;
5. evidence sufficient to decide whether research with users or patient data is
   appropriate.

No real-world study, pilot, or deployment is authorized by this document.
