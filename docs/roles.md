# Roles del equipo — clinical-nlp-triage-open-source

Este documento define los roles principales del proyecto y orienta cómo puede contribuir cada perfil. El objetivo es facilitar la colaboración entre perfiles clínicos, ingeniería biomédica, NLP, ciencia de datos y documentación, trabajando de forma asincrónica y en diferentes zonas horarias.

---

## 1. Project Lead (Coordinación general)

**Responsable:** Alfredo Martin Gil (Médico + IA en salud)

**Responsabilidades principales:**
- Definir la visión global del proyecto y el roadmap.
- Priorizar tareas y decidir qué entra en cada versión.
- Asegurar que las decisiones técnicas respeten los principios de seguridad y ética en salud.
- Aprobar cambios que afecten a la parte clínica o al objetivo del proyecto.

**Decisiones:**  
Tiene la última palabra cuando hay conflicto entre velocidad de desarrollo y seguridad clínica.

---

## 2. Clinical Lead(s)

**Perfil:** médicos/as, enfermería, profesionales sanitarios.

**Responsabilidades:**
- Validar criterios de red flags y reglas clínicas.
- Revisar cambios en el lexicon.
- Ayudar a definir o validar el ground truth anotado.
- Evaluar riesgos clínicos (infra-detección, sobre-triage, ambigüedad).

**Ejemplos de tareas:**
- Evaluar términos del lexicon y su relevancia clínica.
- Revisar outputs del modelo en ejemplos clínicos simulados.
- Proponer mejoras en la lógica de triage basada en práctica real.

---

## 3. Biomedical Engineer / Bioengineer Lead

**Responsable:** Carina Herrera (Bioingeniera)

**Perfil:** ingenieros/as biomédicos, bioingenieros, perfiles híbridos técnica-clínica.

**Responsabilidades:**
- Ser puente entre clínica y tecnología.
- Asegurar la coherencia fisiológica y biomédica del sistema.
- Participar en el diseño de datasets clínicos (vitals, escalas, parámetros).
- Evaluar integraciones futuras con señales fisiológicas o dispositivos simples.
- Revisar estándares biomédicos relevantes (SNOMED-CT, LOINC, etc. si aplica más adelante).

**Ejemplos de tareas:**
- Ajustar o revisar cómo se representan parámetros fisiológicos.
- Proponer reglas de seguridad basadas en fisiología.
- Evaluar si los síntomas y señales están correctamente codificados.
- Proponer mejoras en la estructura de datos clínicas sintéticas.

---

## 4. Bioengineer Contributors

**Perfil:** colaboradores con formación biomédica o interés en datos clínicos.

**Tareas típicas:**
- Ayudar en la creación de datasets sintéticos realistas.
- Validar la coherencia de parámetros fisiológicos.
- Proponer nuevos ejemplos clínicos de alta utilidad.

---

## 5. NLP / ML Lead

**Perfil:** expertos en PLN o modelos de aprendizaje automático.

**Responsabilidades:**
- Diseñar modelos más allá del baseline (embeddings, transformers).
- Proponer y revisar mejoras de tokenización y preprocesamiento.
- Definir métricas avanzadas y protocolos de evaluación.

**Ejemplos de tareas:**
- Proponer modelo con embeddings para v0.1.1.
- Diseñar el módulo de `negation handling`.
- Añadir métricas específicas por categoría de red flags.

---

## 6. Data Engineer / MLOps

**Perfil:** ingeniería de datos, DevOps, MLOps.

**Responsabilidades:**
- Mantener pipeline reproducible.
- Estructurar datasets y versiones.
- Automatizar procesos si es necesario.

**Ejemplos de tareas:**
- Limpieza de datos sintéticos.
- Scripts para regenerar predictions.csv.
- Configurar entornos (requirements, Docker, etc.).

---

## 7. NLP / ML Contributors

**Perfil:** estudiantes, desarrolladores o investigadores en NLP/ML.

**Responsabilidades:**
- Implementar mejoras en tareas definidas en issues.
- Probar nuevas ideas en ramas separadas.
- Documentar resultados.

---

## 8. Clinical Contributors

**Perfil:** profesionales sanitarios que no actúan como Lead.

**Responsabilidades:**
- Proponer ejemplos clínicos sintéticos realistas.
- Revisar outputs.
- Sugerir nuevas categorías o ajustar prioridades.

---

## 9. Documentation & Communication

**Perfil:** personas con buena redacción técnica.

**Responsabilidades:**
- Mantener documentación clara y actualizada.
- Crear guías breves y documentos de referencia.
- Ayudar a ordenar la estructura de `docs/`.

**Ejemplos de tareas:**
- Mejorar `baseline_scoring.md`.
- Redactar guías para nuevos contribuidores.
- Crear changelogs o resúmenes de versiones.

---

## 10. Good First Issue Contributors

**Perfil:** personas nuevas en el proyecto o en IA en salud.

**Responsabilidades:**
- Tomar tareas sencillas marcadas como `good first issue`.
- Reportar reproducibilidad y errores menores.
- Ayudar a mejorar documentación básica.

---

## 11. Nivel de compromiso esperado

Como proyecto open-source:

- No se espera dedicación full-time.
- Los contribuidores participan según disponibilidad.
- Se espera comunicación clara, trabajo documentado y evitar romper el baseline sin aviso.

---

## 12. Toma de tareas

- Las tareas se publican en **Issues**.
- Cada persona puede comentar:  
  > "Me gustaría trabajar en esta tarea."
- Se crea rama (`feature/...`) y luego un Pull Request.

---

## 13. Escalado de dudas

- Dudas clínicas → Clinical Lead / Project Lead.  
- Dudas biomédicas → Bioengineer Lead.  
- Dudas técnicas → NLP/ML Lead o Data Engineer.  
- Organización general → Project Lead.

---

El objetivo es que nadie se quede bloqueado en silencio: es mejor preguntar temprano que corregir tarde en un proyecto de salud.

---
