#!/usr/bin/env python3
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../resources/skills/repository-manager/core'))
import validate_repo
if __name__ == "__main__":
    validate_repo.main() if hasattr(validate_repo, 'main') else os.system('python3 ' + os.path.join(os.path.dirname(__file__), '../resources/skills/repository-manager/core/validate_repo.py'))
