# Guía de Diseño: Workflows Declarativos

Un workflow es un contrato de intención. Sigue estas reglas para crear procesos robustos.

## Estructura Obligatoria
Todo workflow debe tener:
- **Precondiciones**: Requisitos semánticos para iniciar.
- **Postcondiciones**: Estado deseado al finalizar.
- **Pasos (Steps)**: Cada paso debe definir un `intent` (Qué) y sus `associations` (Con qué).

## Validación Estructural (CUE)
Puedes blindar tus workflows vinculando esquemas CUE para validar el estado o los datos:

```yaml
state_validation:
  pre_state_schema: "Topology"
  post_state_schema: "Topology"

steps:
  - id: mi_paso
    intent: "Hacer algo"
    validation:
      input_schema: "MyInput"
      output_schema: "MyOutput"
    associations: [...]
```

## Asociaciones de Fuerza
Usa la escala de 0.0 a 1.0 para indicar la idoneidad de una herramienta. El motor garantiza **exclusión mutua**: un paso puede tener una `tool` o un `workflow`, pero nunca ambos.

## Ejemplo de Anatomía
```yaml
id: mi-proceso
kind: workflow
preconditions: ["Contexto cargado"]
postconditions: ["Resultado verificado"]
steps:
  - id: paso_1
    intent: "Hacer algo importante"
    associations:
      - tool: mi-skill
        strength: 1.0
```
