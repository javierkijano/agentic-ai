from engine import WorkflowEngine

engine = WorkflowEngine("/home/jq-hermes-01/git-repositories/own/agentic-ai-resources")

# Contexto con Topology INVÁLIDA (falta el campo 'owner' que es requerido en workspace.cue)
context = {
    "workspace_state": {
        "workspace": {
            "id": "test-ws"
            # Falta 'owner'
        }
    }
}

print("--- Iniciando Prueba de Validación CUE ---")
engine.execute_workflow("skills-canon-promotion", context=context)
