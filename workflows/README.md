# Guía de Diseño: Workflows Declarativos

Un workflow es un contrato de intención. Sigue estas reglas para crear procesos robustos.

## Estructura Obligatoria
Todo workflow debe tener:
- **Precondiciones**: Requisitos semánticos para iniciar.
- **Postcondiciones**: Estado deseado al finalizar.
- **Pasos (Steps)**: Cada paso debe definir un `intent` (Qué) y sus `associations` (Con qué).

## Asociaciones de Fuerza
Usa la escala de 0.0 a 1.0 para indicar la idoneidad de una herramienta:
- `1.0`: Herramienta óptima y específica.
- `0.5`: Herramienta genérica de apoyo.
- `0.1`: Fallback de emergencia.

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
