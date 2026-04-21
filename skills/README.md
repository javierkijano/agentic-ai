# El Ecosistema de Skills (Habilidades)

Las `skills` son las herramientas atómicas que el agente (`Cortex`) puede usar para ejecutar los `workflows`. A diferencia de los workflows (que son mapas declarativos), las skills contienen lógica ejecutable (`interfaces`).

## Contrato Obligatorio (`resource.yaml`)
Cada skill en este ecosistema debe definir su contrato siguiendo el esquema `protocols/schemas/skill.cue`. Este archivo no solo es documentación, es la **llave de acceso**. Sin un `resource.yaml` válido, el Cortex no podrá instanciar la herramienta.

### Interfaz de Ejecución
```yaml
interfaces:
  cli:
    enabled: true
    commands:
      evaluate: core/logic/evaluator.py
```
El motor delega la acción a estos comandos definidos en las interfaces.

### Sistema de Dependencias (Bidireccionalidad)
Las skills no existen en el vacío. Pueden declarar dependencias entre sí en su bloque `dependencies.skills`:

- **Hard Dependencies (`type: hard`)**: La skill actual *no puede funcionar* sin la dependencia. El sistema de validación exigirá su presencia para levantar el entorno.
- **Soft Dependencies (`type: soft`)**: Relación opcional. Permite al Cortex saber que, si ambas skills están presentes (ej. `repo-management` y `cortex-evaluator`), pueden colaborar o delegar tareas entre ellas (ej. el evaluador auditando un cambio antes del commit). Si la dependencia no está, la skill usará su propio *fallback*.

## Desarrollo de Skills (`dev` -> `core`)
Las skills se desarrollan en el Workspace. Una vez son probadas y estables, se promocionan al Canon (`agentic-ai-resources`) mediante el workflow `skills-canon-promotion`, el cual se encarga de validar la integridad, realizar auditoría de seguridad y documentar recursivamente la nueva habilidad global.
