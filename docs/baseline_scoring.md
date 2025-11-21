# 1. Introducción

## Propósito del baseline
Establecer una línea base mínima para la detección automática de red flags clínicos en notas sintéticas de triaje utilizando un enfoque simple basado en lexicones. Este baseline NO pretende ser clínicamente seguro, sino ofrecer un punto de comparación para futuras versiones más avanzadas (v0.1.1 en adelante).

## Contexto del proyecto clinical-nlp-triage-open-source
El proyecto busca desarrollar un asistente de triaje abierto, reproducible y diseñado para equipos multidisciplinarios trabajando de forma asincrónica en múltiples zonas horarias. El objetivo final es explorar cómo el NLP clínico puede apoyar la orientación inicial de pacientes en contextos con baja disponibilidad médica.

# 2. Dataset utilizado

## Fuente y tipo de datos
Se utiliza el archivo notes_synthetic.csv, compuesto por notas médicas sintéticas generadas para evitar cualquier presencia de PHI.

## Estructura
Columnas incluidas:
- id
- text
- label_redflag (solo si aplica)

Incluye descripciones clínicas básicas: síntomas, contexto, motivo de consulta y pistas del estado general del paciente.

## Consideraciones éticas
- Todos los datos son generados artificialmente.
- No existe ningún tipo de información sensible.
- El dataset puede ser distribuido íntegramente bajo licencia open-source.

# 3. Pipeline del baseline

## Librerías utilizadas
- pandas
- re
- scikit-learn (solo métricas)

## Tokenización
Tokenización simple basada en espacios. No se usa tokenización clínica avanzada.

## Normalización mínima
- Conversión a minúsculas
- Eliminación de símbolos básicos
- Sin stemming ni lematización

## Lógica de detección de red flags (lexicon-based)
El pipeline compara cada texto con un conjunto de términos críticos definidos en lexicon_redflags.csv.
Si encuentra uno o más términos → se marca como red flag.

## Scoring inicial
Salida binaria:
- 1 = red flag detectado
- 0 = sin red flag detectado

# 4. Métricas aplicadas

### Precision
Proporción de true positives frente al total de detecciones.

### Recall
Capacidad para detectar todos los casos relevantes.

### F1-score
Media armónica entre precision y recall.

## Limitaciones del enfoque lexicón
- No reconoce contexto clínico real.
- No detecta negaciones (“no dolor en el pecho”).
- No distingue gravedad.
- No interpreta lenguaje natural coloquial del paciente.
- Alta tasa esperada de falsos positivos/negativos.

## Por qué este baseline NO es clínicamente seguro
- No comprende relaciones anatómicas ni temporales.
- No diferencia síntomas críticos de síntomas inespecíficos.
- Expone a errores graves de subdetección.

# 5. Resultados del baseline

### Tabla de métricas (pendiente de resultados finales)

| Métrica | Valor |
|--------|--------|
| Precision | X.XX |
| Recall | X.XX |
| F1-Score | X.XX |

### Ejemplos de detecciones correctas
- “dolor en el pecho” → detectado
- “hemoptisis” → detectado

### Falsos negativos
- “me falta el aire cuando camino” (no aparece la palabra exacta)

### Falsos positivos
- “tengo miedo de estar grave” (no indica red flag real)

## Interpretación técnica
El baseline es extremadamente simple pero útil como primera referencia cuantitativa. Su objetivo es mostrar limitaciones reales, no ofrecer un rendimiento aceptable.

# 6. Limitaciones del baseline
- Sin modelado contextual
- Sin desambiguación semántica
- No reconoce negaciones clínicas
- Dependencia total del lexicon
- Ambigüedad clínica sin resolver
- No representa lenguaje cotidiano real
- Sin embeddings, sin modelos pre-entrenados, sin razonamiento

# 7. Próximos pasos hacia v0.1.1
- Integrar embeddings (FastText, ClinicalBERT, etc.)
- Mejorar el lexicon con revisión médica
- Añadir reglas basadas en clinical reasoning
- Crear ground truth anotado por médicos del proyecto
- Establecer benchmarks mínimos por categoría
- Añadir módulo de negation handling

# 8. Consideraciones de seguridad y ética
- Riesgo de infra-detección en síntomas críticos
- Riesgo de sobre-triage
- Necesidad de validación humana en cada iteración
- Modelo no apto para uso clínico
- En línea con los principios de IA segura, explicable y responsable

# 9. Conclusión
Este baseline sirve como punto de partida reproducible para evaluar mejoras progresivas. Proporciona una estructura mínima desde la cual construir versiones más sofisticadas, seguras y clínicamente relevantes.

# 10. Reproducibilidad

## Requisitos
- Python 3.10+
- Librerías listadas en requirements.txt

## Pasos
1. Ejecutar notebooks/triage_rules_baseline.ipynb
2. Generar predictions.csv
3. Ejecutar script de métricas
4. Confirmar resultados equivalentes a los publicados

## Semillas
- seed = 42

# 11. Cómo contribuir (resumen)
- Crear branch: feature/nombre
- Crear PR con explicación clara
- Añadir ejemplos cuando corresponda
- Mantener estilo PEP8
- Cambios en el lexicon requieren revisión médica

# 12. Diccionario de conceptos
- Red flag: signo/síntoma que indica riesgo elevado
- Token: unidad mínima (palabra)
- Lexicon: lista de términos críticos
- Embedding: vector semántico
- Negation handling: reconocimiento de negaciones

# 13. Scope / Out of Scope

## Scope
- Pipeline lexicon-based
- Detección binaria simple
- Métricas básicas

## Out of Scope
- Uso clínico real
- Modelos avanzados (transformers)
- Diagnóstico automatizado
- Razonamiento clínico profundo

# 14. Roadmap compacto
- Añadir embeddings → prioridad alta
- Crear ground truth clínico
- Reglas clínicas basadas en reasoning
- Negation detection
- Ampliar lexicon con categorías nuevas
- Mejorar documentación

# 15. Riesgos técnicos y mitigación

| Riesgo | Mitigación |
|--------|------------|
| Data leakage | Aislar dataset y logs |
| Sobreajuste | Evitar tuning prematuro |
| Ambigüedad clínica | Reglas clínicas + revisión médica |
| Lenguaje no estándar | Expandir dataset sintético |

# 16. Plan de validación futura
- Validación médica por profesionales
- Ground truth comparativo
- Evaluación de seguridad
- Documentación de fallos críticos
- Auditoría continua del pipeline
