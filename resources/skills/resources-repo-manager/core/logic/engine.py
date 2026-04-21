#!/usr/bin/env python3
import yaml
import os
from pathlib import Path

class WorkflowEngine:
    def __init__(self, resources_root):
        self.resources_root = Path(resources_root)

    def execute_workflow(self, workflow_id, context=None):
        """
        Orquesta una secuencia de intenciones. 
        NO ejecuta scripts; invoca Skills o Sub-workflows.
        """
        print(f"\n🎭 Orquestando Workflow: {workflow_id}")
        wf_path = self.resources_root / f"resources/workflows/{workflow_id}/resource.yaml"
        
        if not wf_path.exists():
            print(f"❌ Error: Workflow '{workflow_id}' no encontrado.")
            return False

        with open(wf_path, "r") as f:
            config = yaml.safe_load(f)

        steps = config.get("steps", [])
        for step in steps:
            print(f"\n  [Intento: {step.get('id')}]")
            print(f"    Descripción: {step.get('intent')}")
            
            # Resolución de asociaciones por fuerza
            associations = step.get("associations", [])
            # El motor debería elegir la de mayor strength que esté disponible
            best_tool = sorted(associations, key=lambda x: x.get('strength', 0), reverse=True)[0]
            
            if "workflow" in best_tool:
                if not self.execute_workflow(best_tool["workflow"], context): return False
            elif "tool" in best_tool:
                print(f"    🛠 Acción: Usando Skill '{best_tool['tool']}' (Fuerza: {best_tool.get('strength')})")
                # Aquí se invocaría la ejecución real de la Skill
        
        return True

if __name__ == "__main__":
    engine = WorkflowEngine("/home/jq-hermes-01/git-repositories/own/agentic-ai-resources")
    # engine.execute_workflow("add-skill")
