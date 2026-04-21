#!/usr/bin/env python3
import yaml
import subprocess
import sys
import os
from pathlib import Path

class WorkflowEngine:
    def __init__(self, resources_root):
        self.resources_root = Path(resources_root)

    def find_workflow(self, workflow_id):
        """Busca el workflow en core o dev."""
        for folder in ["core", "dev"]:
            path = self.resources_root / f"workflows/{folder}/{workflow_id}/resource.yaml"
            if path.exists():
                return path
        return None

    def execute_workflow(self, workflow_id, context=None):
        print(f"\n🧠 [CORTEX] Orquestando Workflow: {workflow_id}")
        wf_path = self.find_workflow(workflow_id)
        
        if not wf_path:
            print(f"❌ Error: Workflow '{workflow_id}' no encontrado en core/ o dev/.")
            return False

        with open(wf_path, "r") as f:
            config = yaml.safe_load(f)

        print(f"📋 Descripción: {config.get('description')}")
        
        steps = config.get("steps", [])
        for step in steps:
            print(f"\n  ▶️ Paso: {step.get('id')}")
            print(f"     Intento: {step.get('intent')}")
            
            associations = step.get("associations", [])
            if associations:
                best = sorted(associations, key=lambda x: x.get('strength', 0), reverse=True)[0]
                if "workflow" in best:
                    self.execute_workflow(best["workflow"], context)
                else:
                    print(f"     🛠 Herramienta Seleccionada: {best.get('tool')} (Fuerza: {best.get('strength')})")
            
            if "shell" in step:
                print(f"     🐚 Ejecutando: {step['shell']}")
                subprocess.run(step["shell"], shell=True, capture_output=True)

        print(f"\n✅ Workflow '{workflow_id}' finalizado.")
        return True

if __name__ == "__main__":
    import sys
    wf_id = sys.argv[1] if len(sys.argv) > 1 else "promote-to-core"
    engine = WorkflowEngine("/home/jq-hermes-01/git-repositories/own/agentic-ai-resources")
    engine.execute_workflow(wf_id)
