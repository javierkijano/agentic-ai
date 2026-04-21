# Agentic Resources - Canonical Gateway

Bienvenido a la fuente de verdad. Este repositorio contiene el ADN del sistema. Como Agente, este es tu **Manual Operativo de Nivel 0**.

## 🧠 El Bucle Maestro (`master-agent-loop`)
Todo empieza y termina aquí. **No tienes permitido realizar acciones directas sobre el código sin estar orquestado por un workflow**.
El `master-agent-loop` es el único camino válido para resolver tareas, y consta de:
1. **Identificación**: Entender qué quiere el usuario.
2. **Revisión Estratégica**: Cuestionar si la tarea tiene sentido arquitectónico.
3. **Planificación**: Presentar al usuario el plan de ejecución (workflows seleccionados).
4. **Ejecución**: Usar el `WorkflowEngine` para orquestar la tarea, validando todo bajo esquemas CUE.
5. **Evaluación**: Aprender del éxito o fracaso del ciclo.
6. **Documentación Recursiva**: Sincronizar todos los manuales y arquitectura (¡incluyendo este mismo archivo!) de forma automática.
7. **Improvement Loop**: Si algo falla o puede mejorar, crear propuestas de mejora y enviarlas al Backlog (`improvement-backlog-review`).

## 🛡️ Autonomía Certificada (CUE Contracts)
Este sistema confía en ti, pero **verifica todo lo que haces**. 
El "Aduanero" (Cortex Engine) usará `cue vet` sobre los archivos `protocols/schemas/*.cue` para bloquear tu ejecución si:
- Creas una Skill con dependencias mal formadas (`Hard` vs `Soft`).
- Omites un campo obligatorio en el Contexto (`context.cue`).
- Propones un Workflow sin validaciones de estado (`state_validation`).

## 🚨 Reglas de Oro Absolutas
1. **Nada existe fuera del Workflow**: Si una tarea no tiene un workflow definido en `workflows/core/`, **debes parar y disparar `create-new-workflow`**.
2. **Documentación como Cierre Obligatorio**: Nunca des una tarea por finalizada sin disparar el workflow de documentación correspondiente (o dejar que el Master Loop lo haga por ti).
3. **Mejora Continua**: Si detectas una fricción sistémica, no la ignores. Extrae el tema, lanza un brainstorming evolutivo y promueve la idea a la cola de mejoras (`backlog.jsonl`).
4. **Trabajo en Worktrees**: Todo código debe modificarse en ramas y worktrees efímeros gestionados por el Workspace. ¡Nunca modifiques la rama `main` de este canon directamente para tareas de usuario final, a menos que sean refactors estructurales autorizados como este!

## 📂 Directorios Clave
- `skills/`: Habilidades atómicas y aisladas (`resource.yaml` obligatorios).
- `workflows/`: Mapas de intención declarativos (`resource.yaml` obligatorios).
- `protocols/schemas/`: Los contratos CUE que definen tu mundo.
- `docs/`: La memoria arquitectónica (Ver `docs/architecture.md`).
