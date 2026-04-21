# Arquitectura del Ecosistema Agentic AI

Este documento define los principios de funcionamiento y la división de responsabilidades del sistema.

## 1. Filosofía de Dos Capas

### A. El Canon (`agentic-ai-resources`)
Es el **Cerebro** y la **Memoria a Largo Plazo**.
- **Inmutable**: No se debe trabajar directamente en sus ramas principales.
- **Universal**: Contiene skills y protocolos que pueden ser usados por cualquier workspace.
- **Responsabilidad**: Definir *qué* puede hacer el sistema.

### B. El Workspace (`agentic-ai-workspace`)
Es el **Cuerpo** y la **Memoria de Trabajo**.
- **Mutable**: Contiene logs, estados temporales, configuraciones locales y Worktrees.
- **Topológico**: Sabe dónde están los proyectos y cómo conectarse a los recursos.
- **Responsabilidad**: Definir *dónde* y *cómo* se ejecutan las tareas.

## 2. Gobernanza: El Master Agent Loop
El ecosistema no es una colección de scripts aislados, es un **organismo auto-orquestado**. La interacción con el sistema siempre ocurre a través del `master-agent-loop`, un ciclo estricto de:
1. **Task Identification & Strategic Review**: Entender qué se pide y cuestionar su viabilidad.
2. **Workflow Selection & Execution**: Construir el plan y delegar al motor.
3. **Evaluation & Recursive Documentation**: Aprender de la ejecución y documentar automáticamente cambios (hasta en diseño o arquitectura).
4. **Continuous Improvement**: Cerrar el bucle analizando fallos y proponiendo mejoras al backlog.

## 3. Autonomía Certificada y Contratos (CUE)
La intención del agente se separa de la ejecución a través de contratos estructurales definidos en `protocols/schemas/*.cue`.
- **El Aduanero**: El `WorkflowEngine` (Cortex) no ejecuta un paso sin validar antes su input, output y cambios de estado contra un esquema CUE.
- **Manifiestos de Cumplimiento (Compliance)**: Cada ciclo genera un archivo forense `.json` en `runtime/compliance/` con el detalle de las validaciones, generando pruebas irrefutables del éxito (`✅ PASS`) o fallo (`❌ FAIL`) estructural del sistema.

## 4. Evolución y Sistema Inmunológico
El sistema está diseñado para trascender la supervivencia técnica mediante dos herramientas:
- **Improvement Loop**: Si el `WorkflowEngine` falla o detecta ineficiencias, genera propuestas de mejora basadas en el manifiesto y los deposita en `runtime/improvements/backlog.jsonl`.
- **Brainstorming Evolutivo**: Constantemente analiza las interacciones (logs, sesiones, memoria), identifica hilos conductores (Thematic Extraction) y propone ideas disruptivas evaluadas en una matriz de Impacto vs. Esfuerzo (Divergent Brainstorming).

## 5. El Ciclo de Vida de una Skill
- **Desarrollo**: Se crea en el Workspace como recurso experimental (`dev`).
- **Promoción**: Se valida contra el esquema `skill.cue` y se mueve al repositorio de Recursos (`core`).
- **Canonización**: Se registra en el `resources/skills/` del Canon para estar disponible globalmente.

## 6. Gestión de Estado (`runtime/`)
El directorio `runtime/` en el Workspace es el único lugar donde se permite la escritura de logs y persistencia de sesión (compliance, improvements) durante la operación normal. El Canon nunca debe contener una carpeta `runtime/` con datos locales.

## 7. Gestión de Dependencias Inter-Skills
El sistema soporta una jerarquía de dependencias para asegurar la robustez y fomentar la composición:

- **Hard Dependencies (Duras)**: Relaciones obligatorias. Si la Skill A tiene una dependencia `hard` de la Skill B, el sistema garantiza que ambas deben estar presentes y validadas para la operación.
- **Soft Dependencies (Blandas)**: Relaciones opcionales y bidireccionales. Permiten que una Skill mejore su comportamiento o delegue capacidades si la dependencia está presente, pero garantiza que la Skill sigue siendo funcional en su ausencia (usando fallbacks internos).
- **Contrato CUE**: Todas las dependencias deben declararse explícitamente en el `resource.yaml` y son validadas estructuralmente por el Cortex antes de la ejecución.
