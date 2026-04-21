# Manual Técnico: Cortex Workflow Engine

El motor de ejecución del Cortex (`engine.py`) es el responsable de interpretar los workflows declarativos y orquestar las capacidades del sistema.

## Capacidades Avanzadas
1. **Transparencia de Planificación**: Antes de cada ejecución, el motor genera una previsualización jerárquica del plan para que el usuario entienda la cadena de acciones.
2. **Certificación de Cumplimiento (Compliance)**: Genera un Manifiesto de Ejecución Certificada (`execution_*.json`) que registra cada validación estructural CUE realizada.
3. **Validación Estructural CUE**: Usa el paquete de esquemas en `protocols/schemas/` para validar el estado del workspace y los inputs/outputs de cada paso.

## Principios de Ejecución
1. **Resolución Dinámica**: El motor busca los workflows en `workflows/core/` y `workflows/dev/`.
2. **Asociación de Fuerza**: Evalúa las `associations` y selecciona la herramienta (Skill) con mayor `strength`.
3. **Anidamiento Recursivo**: Soporta la ejecución de sub-workflows de forma transparente y certificada.

## Uso desde CLI
```bash
python3 skills/cortex/step-executor/engine.py <workflow-id>
```
