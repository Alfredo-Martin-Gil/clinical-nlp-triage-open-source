# Contribution Guide — clinical-nlp-triage-open-source

Thank you for your interest in contributing to **clinical-nlp-triage-open-source**!  
This project explores how clinical NLP can support triage and early orientation in contexts with limited medical availability, always from a perspective of **safe, responsible, and open artificial intelligence**.

This document explains how to contribute in an organized, safe, and meaningful way for the team.

---

## 1. Project principles

- This is **not** a clinical care project and must **not** be used for real clinical decision-making.
- Safety and ethics take precedence over development speed.
- Reproducibility and transparency are fundamental.
- Multidisciplinary collaboration (clinical + bioengineering + NLP + data + documentation) is the core of the project.

---

## 2. Roles and responsibilities

Roles are described in detail in:

- `docs/roles.md`

They include:

- Project Lead  
- Clinical Lead(s)  
- **Bioengineer Lead**  
- **Bioengineer Contributors**  
- NLP / ML Lead  
- Data Engineer / MLOps  
- NLP / ML Contributors  
- Clinical Contributors  
- Documentation & Communication  
- Good First Issue Contributors  

Each contributor should review this document before taking on a task.

---

## 3. Types of contributions welcome

### 🧠 Clinical
- Validation of red flags.
- Review of synthetic cases.
- Proposal of triage rules based on real clinical practice.

### 🧬 Bioengineering  
*(Newly incorporated role)*

- Validation of physiological parameters (SpO₂, HR, RR, BP, temperature).
- Design or review of synthetic clinical datasets.
- Suggestions based on physiology, biometrics, or signals.
- Evaluation of biomedical coherence in triage rules.
- Review of biomedical terminology or standards (SNOMED, LOINC… if applicable).

### 🤖 NLP / ML
- Improvements in tokenization, embeddings, models, negation handling.
- Experimentation with new models.
- Error analysis and metric evaluation.

### 🗂️ Data
- Improvement of dataset structures.
- Generation of new synthetic examples.
- Cleaning and preprocessing.

### 📝 Documentation
- Improve `README.md`, `baseline_scoring.md`, `roles.md`.
- Create guides for new contributors.
- Document experiments or significant changes.

---

## 4. Recommended workflow

### 4.1. Choose a task
1. Go to the **Issues** tab.
2. Look for labels such as:  
   - `clinical`  
   - `bioengineering`  
   - `NLP`  
   - `data`  
   - `documentation`  
   - `good first issue`
3. Comment:  
   > "I would like to work on this issue. May I take it?"

### 4.2. Create a branch or fork
If you have permissions:
- Create a branch from `main`, for example:  
  - `feature/short-name`  
  - `bioeng/physiological-parameters`  
  - `clinical/redflags-chest-pain`  
  - `nlp/embeddings-v0-1-1`

If you do not have permissions:
- Fork the repository.

### 4.3. Make changes
- Keep changes focused on a single task.
- Document important decisions.
- Update documentation if behavior changes.

### 4.4. Open a Pull Request
- Reference the issue:  
  > “Closes #12”
- Explain:  
  - What was done  
  - Why  
  - How it was tested  
- If clinical or biomedical logic is affected, state it explicitly.

---

## 5. Code and style standards

### Language
- Python 3.10+

### Style
- PEP8
- Descriptive variable names
- Comments only when they add meaningful context

### File locations
- `data/` → datasets  
- `notebooks/` → notebooks  
- `src/` → scripts  
- `docs/` → technical documentation  

---

## 6. Clinical and biomedical changes

### 6.1. Clinical changes
Any change affecting clinical rules or red flags requires:
- A prior issue  
- Review by a Clinical Lead or Project Lead  

### 6.2. Biomedical changes
Any change affecting physiological parameters, clinical data structures, physiology-based criteria, or device-related concepts requires:

- An issue labeled `bioengineering`
- Review by the Bioengineer Lead
- Clear physiological or biomedical justification

### 6.3. Changes to the red-flag lexicon
Must be reviewed by:
- A Clinical Lead  
- Or a Bioengineer Lead (if physiological parameters are involved)

---

## 7. Baseline reproducibility

Before submitting a PR that affects the baseline:

1. Confirm the notebook runs without errors.
2. Regenerate `predictions.csv`.
3. Verify that metrics are maintained or improved.
4. Update documentation if results change.

---

## 8. Bug reporting

Create an issue including:
- Clear description of the bug  
- Steps to reproduce  
- Python version  
- Involved files  

Label when possible:
- `bug`
- `clinical`
- `bioengineering`
- `NLP`
- `documentation`

---

## 9. New features

Open an issue labeled `enhancement` or `feature request`.

Explain:
- What problem it addresses  
- Clinical or biomedical risks  
- Impact on triage or safety  
- Required changes to data or logic  

---

## 10. Code of conduct (summary)

- Respect among collaborators.  
- Clear communication without unnecessary jargon.  
- Discrimination or personal attacks are not tolerated.  
- The Project Lead may intervene to mediate conflicts.

---

## 11. Questions and support

If you have questions:
- Comment on an existing issue  
- Or open a new issue labeled `question`

---

Thank you for being part of this healthcare AI project.  
Every contribution, no matter how small, helps build tools that are more transparent, safer, and more useful for the community.


# Guía de contribución — clinical-nlp-triage-open-source

¡Gracias por tu interés en colaborar con **clinical-nlp-triage-open-source**!  
Este proyecto explora cómo el NLP clínico puede ayudar al triaje y orientación inicial en contextos con baja disponibilidad médica, siempre desde una perspectiva de **IA segura, responsable y abierta**.

Este documento explica cómo contribuir de forma ordenada, segura y útil para el equipo.

---

## 1. Principios del proyecto

- Este no es un proyecto asistencial ni debe usarse para decisiones clínicas reales.
- La seguridad y ética están por encima de la velocidad de desarrollo.
- La reproducibilidad y la transparencia son fundamentales.
- La colaboración multidisciplinaria (clínica + bioingeniería + NLP + datos + documentación) es el núcleo del proyecto.

---

## 2. Roles y responsabilidades

Los roles se encuentran descritos en detalle en:

- `docs/roles.md`

Incluyen:

- Project Lead  
- Clinical Lead(s)  
- **Bioengineer Lead**  
- **Bioengineer Contributors**  
- NLP / ML Lead  
- Data Engineer / MLOps  
- NLP/ML Contributors  
- Clinical Contributors  
- Documentation & Communication  
- Good First Issue Contributors  

Cada contribuyente debe revisar este documento antes de asumir una tarea.

---

## 3. Tipos de contribuciones bienvenidas

### 🧠 Clínica
- Validación de red flags.
- Revisión de casos sintéticos.
- Propuesta de reglas de triaje basadas en práctica real.

### 🧬 Bioingeniería
*(Nuevo rol incorporado)*

- Validación de parámetros fisiológicos (SpO₂, FC, FR, PA, temperatura).
- Diseño o revisión de datasets clínicos sintéticos.
- Sugerencias basadas en fisiología, biometría o señales.
- Evaluación de coherencia biomédica en reglas de triaje.
- Revisión de terminología o estándares biomédicos (SNOMED, LOINC… si aplica).

### 🤖 NLP / ML
- Mejoras en tokenización, embeddings, modelos, negation handling.
- Experimentación con modelos nuevos.
- Análisis de errores y métricas.

### 🗂️ Datos
- Mejora de estructuras de datasets.
- Generación de nuevos ejemplos sintéticos.
- Limpieza y preprocesamiento.

### 📝 Documentación
- Mejorar `README.md`, `baseline_scoring.md`, `roles.md`.
- Crear guías para nuevos colaboradores.
- Documentar experimentos o cambios importantes.

---

## 4. Flujo de trabajo recomendado

### 4.1. Elegir una tarea
1. Ir a la pestaña **Issues**.
2. Buscar etiquetas como:  
   - `clinical`  
   - `bioengineering`  
   - `NLP`  
   - `data`  
   - `documentation`  
   - `good first issue`
3. Comentar:  
   > "Quiero trabajar en esta issue. ¿Puedo tomarla?"

### 4.2. Crear una rama o fork
Si tenés permisos:
- Crear rama desde `main`:  
  - `feature/nombre-corto`  
  - `bioeng/parametros-fisiologicos`  
  - `clinical/redflags-chest-pain`  
  - `nlp/embeddings-v0-1-1`

Si no tenés permisos:
- Crear un fork del repositorio.

### 4.3. Hacer los cambios
- Mantener cambios enfocados en una sola tarea.
- Documentar decisiones importantes.
- Actualizar documentación si el comportamiento cambia.

### 4.4. Abrir un Pull Request
- Referenciar la issue:  
  > “Closes #12”
- Explicar:  
  - Qué se hizo  
  - Por qué  
  - Cómo se probó  
- Si afecta lógica clínica o biomédica, marcarlo explícitamente.

---

## 5. Estándares de código y estilo

### Lenguaje
- Python 3.10+

### Estilo
- PEP8
- Variables descriptivas
- Comentarios solo si aportan contexto

### Ubicación de archivos
- `data/` → datasets  
- `notebooks/` → notebooks  
- `src/` → scripts  
- `docs/` → documentación técnica  

---

## 6. Cambios clínicos y biomédicos

### 6.1. Cambios clínicos
Todo cambio que afecte reglas clínicas o red flags requiere:
- Issue previa  
- Revisión por Clinical Lead o Project Lead  

### 6.2. Cambios biomédicos
Todo cambio que afecte parámetros fisiológicos, estructura de datos clínicos, criterios basados en fisiología o dispositivos requiere:

- Issue bajo etiqueta: `bioengineering`
- Revisión del Bioengineer Lead
- Justificación fisiológica o biomédica clara

### 6.3. Cambios en el lexicon de red flags
Debe ser revisado por:
- Clinical Lead  
- O Bioengineer Lead (si aplica parámetros o fisiología)

---

## 7. Reproducibilidad del baseline

Antes de realizar un PR que afecte el baseline:

1. Confirmar que el notebook se ejecuta sin errores.
2. Regenerar `predictions.csv`.
3. Verificar que las métricas se mantienen o mejoran.
4. Actualizar documentación si cambian resultados.

---

## 8. Reporte de bugs

Crear una issue con:
- Descripción clara del error  
- Pasos para reproducir  
- Versión de Python  
- Archivos involucrados  

Etiquetar si es posible:
- `bug`
- `clinical`
- `bioengineering`
- `NLP`
- `documentation`

---

## 9. Nuevas funcionalidades

Abrir issue tipo `enhancement` o `feature request`.

Explicar:
- Qué problema resuelve  
- Riesgos clínicos o biomédicos  
- Impacto en triaje o seguridad  
- Cambios que implica en datos o lógica  

---

## 10. Código de conducta (resumen)

- Respeto entre colaboradores.  
- Comunicación clara y sin tecnicismos innecesarios.  
- No se tolera discriminación ni ataques personales.  
- El Project Lead puede intervenir para mediar conflictos.

---

## 11. Preguntas y soporte

Si tenés dudas:
- Comentar en una Issue  
- Abrir Issue con etiqueta `question`  


---

¡Gracias por formar parte de este proyecto de IA en salud! 
Cada contribución, por pequeña que parezca, ayuda a construir herramientas más transparentes, seguras y útiles para la comunidad.
