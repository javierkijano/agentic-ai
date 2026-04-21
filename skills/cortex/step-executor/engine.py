#!/usr/bin/env python3
import yaml
import subprocess
import sys
from pathlib import Path
import tempfile
import os

class WorkflowEngine:
    def __init__(self, resources_root):
        self.resources_root = Path(resources_root)
        self.schemas_root = self.resources_root / "protocols/schemas"

    def find_workflow(self, workflow_id):
        for folder in ["core", "dev"]:
            path = self.resources_root / f"workflows/{folder}/{workflow_id}/resource.yaml"
            if path.exists():
                return path
        return None

    def validate_structural_contract(self, data, schema_name, definition_name=None):
        """Valida datos (dict) contra un esquema CUE."""
        if not schema_name or data is None:
            return True

        cue_file = self.schemas_root / f"{schema_name}.cue"
        if not cue_file.exists():
            print(f"⚠️ Aviso: Esquema CUE '{schema_name}.cue' no encontrado. Saltando validación.")
            return True

        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as tf:
            yaml.dump(data, tf)
            temp_path = tf.name

        try:
            # Comando: cue vet <datos.yaml> <esquema.cue> -d <Definicion>
            cmd = ["cue", "vet", temp_path, str(cue_file)]
            if definition_name:
                cmd.extend(["-d", f"#{definition_name}"])

            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"❌ Error de Validación Estructural (CUE): {schema_name}")
                print(result.stderr)
                return False
            return True
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def execute_workflow(self, workflow_id, context=None, is_preview=False):
        context = context or {}
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

        # 1. Validación de Estado Previo (CUE)
        state_v = config.get("state_validation", {})
        if not is_preview and state_v.get("pre_state_schema"):
            if not self.validate_structural_contract(context.get("workspace_state", {}), "workspace", state_v["pre_state_schema"]):
                return False

        steps = config.get("steps", [])
        for step in steps:
            prefix = "    └─" if is_preview else "  ▶️ Paso:"
            print(f"{prefix} {step.get('id')} ({step.get('intent')[:60]}...)")

            # 2. Validación de Input por Paso
            step_v = step.get("validation", {})
            if not is_preview and step_v.get("input_schema"):
                if not self.validate_structural_contract(context.get("last_input", {}), "base", step_v["input_schema"]):
                    return False

            associations = step.get("associations", [])
            if associations:
                best = sorted(associations, key=lambda x: x.get('strength', 0), reverse=True)[0]
                if "workflow" in best:
                    self.execute_workflow(best["workflow"], context, is_preview=True)
                elif not is_preview:
                    print(f"     🛠 Herramienta Seleccionada: {best.get('tool')} (Fuerza: {best.get('strength')})")

            # 3. Validación de Output por Paso
            if not is_preview and step_v.get("output_schema"):
                if not self.validate_structural_contract(context.get("last_output", {}), "base", step_v["output_schema"]):
                    return False

        # 4. Validación de Estado Posterior
        if not is_preview and state_v.get("post_state_schema"):
             if not self.validate_structural_contract(context.get("workspace_state", {}), "workspace", state_v["post_state_schema"]):
                return False

        if not is_preview:
            print(f"\n✅ Workflow '{workflow_id}' finalizado.")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: engine.py <workflow_id>")
        sys.exit(1)
    
    wf_id = sys.argv[1]
    engine = WorkflowEngine("/home/jq-hermes-01/git-repositories/own/agentic-ai-resources")
    engine.execute_workflow(wf_id)
