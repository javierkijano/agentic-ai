#!/usr/bin/env python3
import os
import sys
import argparse
import yaml
from logger import log_operation

def create_resource(res_type, res_id):
    base_path = f"resources/{res_type}/{res_id}"
    
    if os.path.exists(base_path):
        log_operation("create_resource", "ERROR", f"Resource {res_id} already exists")
        print(f"ERROR: Resource '{res_id}' of type '{res_type}' already exists at {base_path}")
        sys.exit(1)
    
    # Standard folder structure
    dirs = [
        "core/logic",
        "core/cli",
        "core/webapp",
        "core/docs",     # For STORAGE.md and other internal docs
        "tests",
        "platforms/hermes"
    ]
    
    for d in dirs:
        os.makedirs(os.path.join(base_path, d), exist_ok=True)
    
    # Create resource.yaml with storage and interfaces
    resource_data = {
        "id": res_id,
        "kind": res_type.rstrip('s'),
        "status": "draft",
        "description": f"Capability for {res_id}",
        "tags": [],
        "platforms": ["hermes", "generic"],
        "interfaces": {
            "cli": {"enabled": True, "commands": {"status": "Check status"}},
            "webapp": {"enabled": False, "port": None, "entrypoint": "app.py"}
        },
        "storage": {
            "standard_layout": True,
            "description": "Defines how this skill handles runtime data",
            "contract": "core/docs/STORAGE.md"
        },
        "depends_on": []
    }
    
    with open(os.path.join(base_path, "resource.yaml"), "w") as f:
        yaml.dump(resource_data, f, sort_keys=False)
    
    # Create STORAGE.md Contract
    storage_md = f"""# Storage Contract: {res_id}

This document defines the expected runtime storage structure for this skill.
Any agent or system executing this skill MUST provide a base directory and adhere to this layout.

## Runtime Structure

The base directory will be provided at runtime (e.g., `runtime/{{context}}/{{resource_id}}/`).

| Path | Type | Description |
|------|------|-------------|
| `logs/` | Directory | Standard output and error logs. |
| `config/` | Directory | Instance-specific configuration files. |
| `state/` | Directory | Persistent state between executions. |
| `data/` | Directory | Temporary or generated assets. |

## Requirements
- Files in `config/` should follow the schemas in `core/schemas/` if available.
- The `state/` directory must be writable by the execution agent.
"""
    with open(os.path.join(base_path, "core/docs/STORAGE.md"), "w") as f:
        f.write(storage_md)
    
    # Create README.md
    with open(os.path.join(base_path, "README.md"), "w") as f:
        f.write(f"# {res_id.replace('-', ' ').title()}\n\nDescription for {res_id}.\n")
        
    log_operation("create_resource", "SUCCESS", f"Created {res_type}/{res_id} with Storage Contract")
    print(f"SUCCESS: Created resource '{res_id}' with standardized Storage Contract.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new agentic resource pack.")
    parser.add_argument("--type", required=True, help="Category (e.g., skills, agents, workflows)")
    parser.add_argument("--id", required=True, help="Resource unique ID (kebab-case)")
    
    args = parser.parse_args()
    create_resource(args.type, args.id)
 Joseph
