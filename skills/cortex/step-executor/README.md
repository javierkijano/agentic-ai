# Manual Técnico: Cortex Workflow Engine

El motor de ejecución del Cortex (`engine.py`) es el responsable de interpretar los workflows declarativos y orquestar las capacidades del sistema.

## Principios de Ejecución
1. **Resolución Dinámica**: El motor busca los workflows en `workflows/core/` y `workflows/dev/`.
2. **Asociación de Fuerza**: Para cada paso, el motor evalúa las `associations` y selecciona la herramienta (Skill) con mayor `strength`.
3. **Anidamiento**: Si una asociación apunta a otro `workflow`, el motor suspende la ejecución actual y entra en el sub-workflow de forma recursiva.
4. **Pureza Declarativa**: El motor prohíbe scripts directos en los workflows para asegurar la portabilidad e independencia técnica.

## Uso desde CLI
```bash
python3 skills/cortex/step-executor/engine.py <workflow-id>
```
