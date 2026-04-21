# Manual Técnico: Cortex Workflow Engine

El motor de ejecución del Cortex (`engine.py`) es el responsable de interpretar los workflows declarativos y orquestar las capacidades del sistema.

## Capacidades Avanzadas
1. **Transparencia de Planificación**: Antes de cada ejecución, el motor genera una previsualización jerárquica del plan para que el usuario entienda la cadena de acciones.
2. **Certificación de Cumplimiento (Compliance)**: Genera un Manifiesto de Ejecución Certificada (`execution_*.json`) en `runtime/compliance/` que registra cada validación estructural CUE realizada (PASS/FAIL).
3. **Mejora Continua**: El Bucle Maestro lee estos manifiestos para nutrir el *Improvement Loop* (proponer ideas y parches al `backlog.jsonl` ante `FAIL`s repetidos).
4. **Validación Estructural CUE**: Usa el paquete de esquemas en `protocols/schemas/` para validar el estado efímero (Contexto mental del Agente), el Workspace y los inputs/outputs de cada paso.

## Modos de Operación (Strictness)
- **Modo Estricto (`strict_mode=True`)**: Configuración por defecto. Utiliza `cue vet` internamente. Aborta la validación si encuentra valores incompletos (`incomplete value`).
- **Modo Flexible (`strict_mode=False`)**: Útil para desarrollo o cuando el Contexto inicial no está totalmente definido. Utiliza `cue eval`, el cual **ignora los campos incompletos**, pero preserva rigurosamente el chequeo de tipos, rangos y restricciones de exclusión.

## Principios de Ejecución
1. **Resolución Dinámica**: El motor busca los workflows en `workflows/core/` y `workflows/dev/`.
2. **Asociación de Fuerza**: Evalúa las `associations` y selecciona la herramienta (Skill) con mayor `strength`.
3. **Anidamiento Recursivo**: Soporta la ejecución de sub-workflows de forma transparente y certificada.

## Uso desde CLI
```bash
python3 skills/cortex/step-executor/engine.py <workflow-id>
```
