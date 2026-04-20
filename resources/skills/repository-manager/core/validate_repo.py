#!/usr/bin/env python3
import os
import yaml
import sys
from logger import log_operation

def validate_layout():
    expected_dirs = [
        'vendor', 'resources', 'contexts', 'shared', 'dist', 'scripts', 'docs'
    ]
    missing = [d for d in expected_dirs if not os.path.isdir(d)]
    if missing:
        log_operation("validate_repo", "ERROR", f"Missing dirs: {missing}")
        print(f"CRITICAL: Missing core directories: {missing}")
        return False
    print("SUCCESS: Core directory structure is valid.")
    return True

def validate_resources():
    valid = True
    resources_root = 'resources'
    for category in os.listdir(resources_root):
        cat_path = os.path.join(resources_root, category)
        if not os.path.isdir(cat_path):
            continue
        
        for resource_id in os.listdir(cat_path):
            res_path = os.path.join(cat_path, resource_id)
            if not os.path.isdir(res_path):
                continue
            
            yaml_path = os.path.join(res_path, 'resource.yaml')
            if not os.path.exists(yaml_path):
                log_operation("validate_repo", "WARNING", f"Resource {resource_id} missing resource.yaml")
                print(f"ERROR: Resource '{resource_id}' in '{category}' is missing resource.yaml")
                valid = False
                continue
            
            try:
                with open(yaml_path, 'r') as f:
                    data = yaml.safe_load(f)
                    required_fields = ['id', 'kind', 'status']
                    for field in required_fields:
                        if field not in data:
                            log_operation("validate_repo", "WARNING", f"Resource {resource_id} missing field {field}")
                            print(f"ERROR: resource.yaml for '{resource_id}' is missing required field: {field}")
                            valid = False
            except Exception as e:
                log_operation("validate_repo", "ERROR", f"Failed to parse yaml for {resource_id}")
                print(f"ERROR: Failed to parse resource.yaml for '{resource_id}': {e}")
                valid = False
    
    if valid:
        print("SUCCESS: All resources validated.")
    return valid

if __name__ == "__main__":
    print("--- Validating Agentic Resources Repository ---")
    layout_ok = validate_layout()
    resources_ok = validate_resources()
    
    if layout_ok and resources_ok:
        log_operation("validate_repo", "SUCCESS", "Full validation passed")
    else:
        log_operation("validate_repo", "FAILURE", "Validation failed")
    
    if not (layout_ok and resources_ok):
        sys.exit(1)
    print("--- Validation Complete ---")
