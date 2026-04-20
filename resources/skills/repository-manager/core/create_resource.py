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
    
    # Create directories
    os.makedirs(os.path.join(base_path, "core"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "tests"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "platforms"), exist_ok=True)
    
    # Create resource.yaml
    resource_data = {
        "id": res_id,
        "kind": res_type.rstrip('s'), # basic normalization
        "status": "draft",
        "source": None,
        "derived_from": None,
        "tags": [],
        "platforms": [],
        "depends_on": []
    }
    
    with open(os.path.join(base_path, "resource.yaml"), "w") as f:
        yaml.dump(resource_data, f, sort_keys=False)
    
    # Create README.md
    with open(os.path.join(base_path, "README.md"), "w") as f:
        f.write(f"# {res_id.replace('-', ' ').title()}\n\nDescription for {res_id}.\n")
        
    log_operation("create_resource", "SUCCESS", f"Created {res_type}/{res_id}")
    print(f"SUCCESS: Created resource '{res_id}' in {base_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new agentic resource pack.")
    parser.get_default('type')
    parser.add_argument("--type", required=True, help="Category (e.g., skills, agents, workflows)")
    parser.add_argument("--id", required=True, help="Resource unique ID (kebab-case)")
    
    args = parser.parse_args()
    
    # Validate type
    valid_types = os.listdir('resources')
    if args.type not in valid_types:
        print(f"ERROR: Invalid type '{args.type}'. Must be one of: {valid_types}")
        sys.exit(1)
        
    create_resource(args.type, args.id)
