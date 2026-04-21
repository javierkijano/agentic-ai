# Validaciones CUE: El Aduanero del Sistema

La capa de esquemas `protocols/schemas/*.cue` reemplaza a JSON Schema como la **Fuente de Verdad Estructural** del ecosistema. CUE aporta herencia, validación de restricciones e integraciones lógicas que impiden que el agente o el usuario inyecten estados corruptos.

## Principios de Diseño
1. **Composición Abierta (`...`)**: Todos los esquemas base (`#Metadata`, `#Topology`, `#Context`) usan el operador `...` al final de su definición. Esto evita errores de `field not allowed` cuando se hereda de ellos (Ej: `Workflow` heredando de `Metadata` y añadiendo el campo `kind`).
2. **Exclusión Mutua**: CUE garantiza lógicamente restricciones complejas. Por ejemplo, en `#Association` (`workflow.cue`), se prohíbe que un paso tenga una `tool` y un `workflow` simultáneamente usando `_|_` (bottom/error).

## Esquemas Clave
- **`context.cue`**: Define la "Memoria a Corto Plazo" (`#Context`). Protege al sistema de ejecutar tareas si faltan metadatos críticos (`goal`, `priority`).
- **`improvement.cue`**: Define el contrato de las propuestas evolutivas (`#ImprovementProposal`), forzando que tengan métricas de brainstorming (`analysis`) y referencias cruzadas (`context_links`).
- **`skill.cue`**: Define las capacidades. Ahora incluye el bloque `dependencies` para relaciones `hard` y `soft`.
- **`workflow.cue`**: Define los mapas de ejecución. Obliga a que los pasos tengan `associations` para conectar intención con ejecución.

## Modos de Estrictez (`strict_mode`)
El `WorkflowEngine` consume estos esquemas de dos maneras:
- **Modo Estricto (`strict_mode=True`)**: Usa `cue vet`. Es implacable. Falla si falta un solo campo obligatorio (`incomplete value`). **Es el modo por defecto para garantizar cumplimiento.**
- **Modo Flexible (`strict_mode=False`)**: Usa `cue eval`. Ignora campos faltantes, pero sigue disparando `FAIL` si hay errores de tipo (ej. `int` en lugar de `string`), rangos fuera de límite, o enums inválidos. Muy útil durante desarrollo o brainstorming cuando el contexto no está completo.
