# Cortex - The Intelligence Engine

El dominio **Cortex** es el responsable de la orquestación, planificación y gobernanza de los procesos del ecosistema. Su función no es realizar tareas físicas, sino **pensar, elegir y supervisar** cómo se realizan dichas tareas usando Workflows.

## Componentes del Cortex

1. **WorkflowSelector**: Dada una orden, identifica qué Workflow de `workflows/core/` o `workflows/dev/` cumple las postcondiciones deseadas.
2. **WorkflowPlanner**: Desglosa el workflow en pasos accionables e inyecta el contexto necesario.
3. **StepExecutor**: El brazo ejecutor que llama a las Skills asociadas a cada paso según su fuerza (`strength`).
4. **CortexEvaluator**: El ojo crítico que verifica si las postcondiciones se cumplieron tras la ejecución.

## Ciclo de Razonamiento del Cortex

Cuando recibes una tarea compleja, debes seguir este flujo mental:
1. **Identificar la Meta**: ¿Qué estado final quiero alcanzar?
2. **Seleccionar**: Busca un workflow cuyas `postconditions` resuelvan esa meta.
3. **Verificar**: ¿Se cumplen las `preconditions`? Si no, planifica una tarea previa para cumplirlas.
4. **Ejecutar**: Llama al `step-executor` para recorrer la cadena de intenciones.
5. **Evaluar**: ¿El estado final es el esperado? Si es así, registra el éxito.

## Maduración de Procesos
Si un proceso en `workflows/dev/` demuestra ser robusto y reutilizable, utiliza el workflow de promoción para moverlo a `workflows/core/`.

---
*La inteligencia no es solo capacidad, es orquestación.*
