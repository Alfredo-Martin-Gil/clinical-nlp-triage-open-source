# Roles del equipo — clinical-nlp-triage-open-source

Este documento define los roles principales del proyecto y orienta cómo puede contribuir cada perfil. La idea es permitir que personas con distinta formación (médicos, ingenieros, científicos de datos, estudiantes, documentalistas) colaboren de forma ordenada y segura.

---

## 1. Project Lead (Coordinación general)

**Responsable:** Alfredo (Médico + IA en salud)

**Responsabilidades principales:**
- Definir la visión global del proyecto y el roadmap.
- Priorizar tareas y decidir qué entra en cada versión (v0.1, v0.2…).
- Asegurar que las decisiones técnicas respeten los principios de seguridad y ética en salud.
- Aprobar cambios que afecten a la parte clínica o al objetivo del proyecto.

**Toma de decisiones:**
- Tiene la última palabra cuando hay conflicto entre velocidad de desarrollo y seguridad clínica.

---

## 2. Clinical Lead(s) (Referentes clínicos)

**Perfil:** médicos/as, enfermería, otros profesionales sanitarios.

**Responsabilidades:**
- Validar los criterios de red flags y las reglas clínicas.
- Ayudar a definir el ground truth anotado.
- Revisar cambios en el lexicon y en las reglas de triage.
- Señalar riesgos clínicos (infra-detección, sobre-triage, ambigüedad).

**Ejemplos de tareas:**
- Revisar propuestas de nuevos términos en `lexicon_redflags.csv`.
- Ayudar a etiquetar ejemplos reales/sintéticos.
- Proponer ajustes de lógica clínica (prioridades, niveles de urgencia).

---

## 3. NLP / ML Lead

**Perfil:** persona con experiencia en NLP y modelos de ML.

**Responsabilidades:**
- Diseñar y revisar los modelos más allá del baseline (embeddings, transformers, etc.).
- Proponer mejoras del pipeline NLP (tokenización, normalización, manejo de negaciones).
- Definir estándares de evaluación (métricas, protocolos de validación).

**Ejemplos de tareas:**
- Añadir un modelo con embeddings (p.ej. ClinicalBERT) para v0.1.1.
- Diseñar el módulo de `negation handling`.
- Proponer nuevas métricas específicas por categoría de red flags.

---

## 4. Data Engineer / MLOps

**Perfil:** ingeniería de datos, MLOps.

**Responsabilidades:**
- Organizar el flujo de datos (datasets, versiones, logs).
- Ayudar a que el pipeline sea reproducible (scripts, automatización).
- Preparar, si es necesario, despliegues mínimos (APIs, demos).

**Ejemplos de tareas:**
- Mantener scripts de preparación de datos.
- Configurar entornos (requirements, Docker, etc.).
- Asegurar que los notebooks se puedan ejecutar sin errores desde cero.

---

## 5. Contributors de NLP / ML

**Perfil:** personas con interés en IA aplicada, NLP, estudiantes o investigadores.

**Responsabilidades:**
- Implementar mejoras propuestas en issues.
- Probar nuevas ideas en ramas separadas.
- Añadir tests y ejemplos.

**Ejemplos de tareas:**
- Mejorar el preprocesamiento de texto.
- Añadir nuevos experimentos de modelos.
- Documentar resultados en nuevos archivos dentro de `docs/`.

---

## 6. Contributors clínicos (no lead)

**Perfil:** médicos/as, enfermería, otros profesionales sanitarios sin carga de coordinación.

**Responsabilidades:**
- Proponer ejemplos clínicos realistas (pero anonimizados o sintéticos).
- Sugerir nuevos red flags o ajustar los existentes.
- Revisar el comportamiento del sistema en casos clínicos simulados.

**Ejemplos de tareas:**
- Revisar outputs de `predictions.csv` en casos de prueba.
- Proponer categorías de triage más ajustadas a la práctica real.
- Validar textos y etiquetas del ground truth.

---

## 7. Documentación y comunicación

**Perfil:** personas con buena redacción técnica, interés en explicar y ordenar.

**Responsabilidades:**
- Mantener la documentación clara y actualizada.
- Ayudar a escribir y mejorar archivos en `docs/` y el README.
- Redactar guías breves para nuevos contribuidores.

**Ejemplos de tareas:**
- Mejorar `baseline_scoring.md` si cambian las métricas.
- Crear guías cortas de “cómo empezar” para colaboradores nuevos.
- Documentar decisiones importantes en un changelog o en issues.

---

## 8. Contributors “good first issue”

**Perfil:** personas que quieren iniciarse en proyectos open-source o en IA en salud.

**Responsabilidades:**
- Empezar por tareas etiquetadas como `good first issue`.
- Preguntar dudas de forma clara en los issues.
- Probar el repositorio, detectar errores básicos, proponer mejoras pequeñas.

**Ejemplos de tareas:**
- Corregir errores menores de documentación.
- Probar pasos de reproducibilidad y reportar si algo falla.
- Sugerir ejemplos adicionales para el dataset sintético.

---

## 9. Nivel de compromiso esperado

Dado que este es un proyecto open-source y multidisciplinario:

- No se espera dedicación full-time.
- Cada rol puede participar según su disponibilidad.
- Lo importante es:
  - Comunicar qué se va a hacer.
  - No romper el baseline sin avisar.
  - Documentar bien los cambios.

---

## 10. Cómo asignar y tomar tareas

- Las tareas se publicarán como **issues** en GitHub.
- Algunas issues estarán marcadas como:
  - `clinical`
  - `NLP`
  - `data`
  - `documentation`
  - `good first issue`
- Cualquier persona puede:
  - Comentar en una issue y decir: “Me gustaría trabajar en esto”.
  - Hacer un fork o una branch y luego abrir un Pull Request (PR).

---

## 11. Escalado de dudas y decisiones

- Dudas clínicas graves → consultar a Clinical Lead / Project Lead.
- Dudas técnicas complejas (modelos, embeddings) → NLP / ML Lead.
- Dudas de flujo de trabajo o organización → Project Lead.

El objetivo es que nadie se quede bloqueado en silencio: es mejor preguntar temprano que corregir tarde en un proyecto de salud.

---
