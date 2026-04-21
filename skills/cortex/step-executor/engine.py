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

    def execute_workflow(self, workflow_id, context=None, is_preview=False):
        if not is_preview:
            print(f"\n🧠 [CORTEX] Ejecutando: {workflow_id}")
        else:
            print(f"  📂 Workflow Planificado: {workflow_id}")

        wf_path = self.find_workflow(workflow_id)
        if not wf_path:
            print(f"❌ Error: Workflow '{workflow_id}' no encontrado.")
            return False

        with open(wf_path, "r") as f:
            config = yaml.safe_load(f)

        steps = config.get("steps", [])
        for step in steps:
            prefix = "    └─" if is_preview else "  ▶️ Paso:"
            print(f"{prefix} {step.get('id')} ({step.get('intent')[:60]}...)")
            
            associations = step.get("associations", [])
            if associations:
                best = sorted(associations, key=lambda x: x.get('strength', 0), reverse=True)[0]
                if "workflow" in best:
                    # En modo preview, bajamos un nivel para mostrar el anidamiento
                    self.execute_workflow(best["workflow"], context, is_preview=True)
                elif not is_preview:
                    print(f"     🛠 Herramienta Seleccionada: {best.get('tool')} (Fuerza: {best.get('strength')})")
            
            if not is_preview and "shell" in step:
                print(f"     🐚 Ejecutando: {step['shell']}")
                subprocess.run(step["shell"], shell=True, capture_output=True)

        if not is_preview:
            print(f"\n✅ Workflow '{workflow_id}' finalizado.")
        return True

if __name__ == "__main__":
    import sys
    wf_id = sys.argv[1] if len(sys.argv) > 1 else "promote-to-core"
    engine = WorkflowEngine("/home/jq-hermes-01/git-repositories/own/agentic-ai-resources")
    engine.execute_workflow(wf_id)
