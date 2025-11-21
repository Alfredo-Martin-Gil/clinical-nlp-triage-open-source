# Guía de contribución — clinical-nlp-triage-open-source

¡Gracias por tu interés en colaborar con **clinical-nlp-triage-open-source**!  
Este proyecto explora cómo el NLP clínico puede apoyar el triaje y la orientación inicial de pacientes en contextos con baja disponibilidad médica, siempre desde una perspectiva de **IA segura, responsable y abierta**.

Este documento explica cómo contribuir de forma ordenada, segura y útil para el equipo.

---

## 1. Principios del proyecto

Antes de contribuir, tené en cuenta que este proyecto:

- **No es un producto asistencial**, ni está destinado a uso clínico directo.
- Es un entorno de experimentación y aprendizaje en IA aplicada a salud.
- Da prioridad a:
  - Seguridad y ética sobre velocidad.
  - Transparencia y reproducibilidad.
  - Trabajo multidisciplinario (clínica + NLP + datos + documentación).

Si en algún momento tenés dudas sobre el impacto clínico o la seguridad de una propuesta, **preguntá antes de implementar**.

---

## 2. Roles y responsabilidades

Los roles del equipo se describen en detalle en:

- `docs/roles.md`

Ahí vas a encontrar:

- **Project Lead** (coordinación general).
- **Clinical Lead(s)** (referentes clínicos).
- **NLP / ML Lead**.
- **Data Engineer / MLOps**.
- **Contributors clínicos, técnicos y de documentación**.
- Issues marcadas como `good first issue` para quienes empiezan.

Te recomendamos leer ese archivo antes de elegir una tarea.

---

## 3. Tipos de contribuciones bienvenidas

Podés contribuir de muchas maneras:

- 🧠 **Clínica**
  - Proponer nuevos red flags o ajustar los existentes.
  - Revisar ejemplos clínicos sintéticos.
  - Ayudar a definir criterios de triaje.

- 🤖 **NLP / ML**
  - Mejorar el preprocesamiento.
  - Proponer modelos nuevos (embeddings, transformers, etc.).
  - Diseñar y evaluar métricas adicionales.

- 🗂️ **Datos**
  - Mejorar la estructura de los datasets sintéticos.
  - Proponer nuevos escenarios clínicos.
  - Ayudar con scripts de preparación de datos.

- 📝 **Documentación**
  - Mejorar `README.md`, `docs/baseline_scoring.md`, `docs/roles.md`.
  - Crear guías para nuevos contribuidores.
  - Documentar experimentos.

- 🧪 **Testing y validación**
  - Probar reproducibilidad del baseline.
  - Revisar outputs de `predictions.csv`.
  - Detectar problemas de seguridad o ambigüedad clínica.

---

## 4. Flujo de trabajo recomendado

### 4.1. Buscar una tarea

1. Ir a la pestaña **Issues** del repositorio.
2. Buscar issues etiquetadas como:
   - `good first issue`
   - `clinical`
   - `NLP`
   - `data`
   - `documentation`
3. Comentá en la issue:  
   > “Me gustaría trabajar en esta tarea. ¿Puedo tomarla?”

### 4.2. Crear rama o fork

Si tenés permisos de escritura:

- Crear una rama desde `main`:
  - `feature/nombre-corto`
  - `fix/bug-descripcion`
  - `doc/actualizacion-baseline`

Si no tenés permisos:

- Hacer un **fork** del repositorio.
- Trabajar en una rama en tu fork.
- Abrir un **Pull Request (PR)** hacia `main`.

### 4.3. Hacer cambios

Recomendaciones:

- Mantener los cambios **enfocados** en una sola cosa por PR.
- Acompañar los cambios de:
  - Comentarios claros en el código si hace falta.
  - Actualización de documentación si se modifica comportamiento.
  - Notas en la issue correspondiente.

### 4.4. Abrir un Pull Request

Al abrir un PR:

- Referenciar la issue relacionada:  
  > “Closes #12” o “Relates to #8”.
- Explicar brevemente:
  - Qué se cambia.
  - Por qué se cambia.
  - Cómo se probó.
- Si el PR afecta lógica clínica o red flags, marcarlo claramente en la descripción.

---

## 5. Estándares de código y estilo

### 5.1. Lenguaje y versión

- Python 3.10+
- Evitar dependencias innecesarias.

### 5.2. Estilo

- Seguir **PEP8**.
- Nombres de variables descriptivos.
- Funciones y módulos con nombres claros.
- Comentarios solo cuando aportan contexto útil.

### 5.3. Estructura esperada

- Datasets en: `data/`
- Notebooks en: `notebooks/`
- Scripts en: `src/`
- Documentación técnica en: `docs/`

Si no estás seguro de dónde ubicar algo, preguntá en la issue.

---

## 6. Cambios clínicos y de seguridad

Esta parte es crítica.

### 6.1. Cambios en el lexicon de red flags

- Todo cambio en `lexicon_redflags.csv` debe ser:
  - Justificado en la issue.
  - Revisado por al menos un **Clinical Lead** o el **Project Lead**.

### 6.2. Cambios en reglas de triage

- Cambios en la lógica que determina la prioridad del paciente **no** deben ser introducidos sin:
  - Discusión previa en una issue.
  - Revisión clínica explícita.

### 6.3. Advertencia

El sistema:

- **No está autorizado para uso asistencial.**
- No reemplaza el juicio clínico.
- No debe utilizarse para tomar decisiones sobre pacientes reales.

---

## 7. Reproducibilidad del baseline

Si tu contribución afecta al baseline, verificá:

1. Que seguís los pasos de `docs/baseline_scoring.md`.
2. Que se puede regenerar `predictions.csv` sin errores.
3. Que las métricas se mantienen o mejoran.
4. Que cualquier cambio relevante quede documentado.

Si los resultados cambian, añadiendo o modificando:

- Explicar por qué.
- Actualizar documentación si procede.

---

## 8. Reporte de bugs y problemas

Si encontrás un problema:

1. Crear una **issue** con:
   - Descripción clara del bug.
   - Pasos para reproducirlo.
   - Entorno (versión de Python, sistema operativo si es relevante).
2. Etiquetarlo, si es posible:
   - `bug`
   - `documentation`
   - `clinical`
   - `NLP`

---

## 9. Propuestas de nuevas funcionalidades

Si tenés una idea nueva:

1. Crear una issue de tipo `enhancement` o `feature request`.
2. Responder brevemente:
   - ¿Qué problema resuelve?
   - ¿Es clínico, técnico o ambos?
   - ¿Hay riesgos clínicos asociados?

No te preocupes si tu propuesta no está totalmente madura: mejor discutirla temprano que implementar algo que luego haya que revertir.

---

## 10. Código de conducta (resumen)

Aunque no haya un archivo formal de código de conducta aún, este proyecto se guía por principios básicos:

- Respeto entre participantes.
- Comunicación clara y honesta.
- No tolerancia a ataques personales, discriminación o acoso.
- Reconocimiento del trabajo ajeno.

Si hay conflictos, el **Project Lead** puede intervenir para mediar.

---

## 11. Preguntas y soporte

Si tenés dudas sobre:

- Cómo empezar.
- Qué tarea elegir.
- Cómo estructurar un PR.
- Cualquier aspecto clínico o técnico.

Podés:

- Comentar en una issue existente.
- Abrir una nueva issue con etiqueta `question`.

---

Gracias por interesarte en este proyecto de IA en salud.  
Cada contribución, por pequeña que parezca, ayuda a construir herramientas más transparentes, seguras y útiles para la comunidad.
