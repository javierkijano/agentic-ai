#!/usr/bin/env python3
import json
import pathlib
import os

class HistoryMiner:
    def __init__(self, workspace_root):
        self.workspace_root = pathlib.Path(workspace_root)
        self.registry_path = self.workspace_root / "runtime/gemini-cli/dev/repository-manager/session_registry.jsonl"
        # Nota: En un entorno real, también leeríamos ~/.hermes_history o archivos de sesión.

    def extract_sequences(self):
        """Extrae secuencias de operaciones del log de trazabilidad."""
        if not self.registry_path.exists():
            return []
        
        sequences = []
        with open(self.registry_path, "r") as f:
            for line in f:
                try:
                    data = json.loads(line)
                    sequences.append({
                        "op": data.get("operation"),
                        "details": data.get("details"),
                        "timestamp": data.get("timestamp")
                    })
                except:
                    continue
        return sequences

    def run(self):
        print("🔍 Minando historial operativo...")
        sequences = self.extract_sequences()
        if not sequences:
            print("⚠️ No se encontraron logs en el registro de sesión.")
            return

        print(f"✅ Se han recuperado {len(sequences)} hitos operativos.")
        for seq in sequences:
            print(f"  - [{seq['op']}]: {seq['details'][:100]}...")

if __name__ == "__main__":
    miner = HistoryMiner("/home/jq-hermes-01/git-repositories/own/agentic-ai-workspace")
    miner.run()
