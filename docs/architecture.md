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
- **Mutable**: Contiene logs, estados temporales y configuraciones locales.
- **Topológico**: Sabe dónde están los proyectos y cómo conectarse a los recursos.
- **Responsabilidad**: Definir *dónde* y *cómo* se ejecutan las tareas.

## 2. Flujo de Datos y Control
1. El Agente inicia en el Workspace.
2. El Workspace consulta el `paths.yaml` para localizar el Canon.
3. El Workspace "importa" la lógica del Canon (vía `sys.path` o wrappers) para ejecutar tareas de gobernanza o gestión.
4. Cualquier cambio en el código se realiza mediante **Worktrees** efímeros, que luego se promocionan al Canon tras ser validados.

## 3. El Ciclo de Vida de una Skill
- **Desarrollo**: Se crea en el Workspace como recurso experimental.
- **Promoción**: Se valida y se mueve al repositorio de Recursos.
- **Canonización**: Se registra en el `resources/skills/` del Canon para ser disponible globalmente.

## 4. Gestión de Estado (`runtime/`)
El directorio `runtime/` en el Workspace es el único lugar donde se permite la escritura de logs y persistencia de sesión durante la operación normal. El Canon nunca debe contener una carpeta `runtime/` con datos locales.

## 5. Gestión de Dependencias Inter-Skills
El sistema soporta una jerarquía de dependencias para asegurar la robustez y fomentar la composición:

- **Hard Dependencies (Duras)**: Relaciones obligatorias. Si la Skill A tiene una dependencia `hard` de la Skill B, el sistema garantiza que ambas deben estar presentes y validadas para la operación.
- **Soft Dependencies (Blandas)**: Relaciones opcionales y bidireccionales. Permiten que una Skill mejore su comportamiento o delegue capacidades si la dependencia está presente, pero garantiza que la Skill sigue siendo funcional en su ausencia (usando fallbacks internos).
- **Contrato CUE**: Todas las dependencias deben declararse en el `resource.yaml` y son validadas estructuralmente por el Cortex antes de la ejecución.
