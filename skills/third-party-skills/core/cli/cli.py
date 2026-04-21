#!/usr/bin/env python3
import sys
import os
import argparse
from pathlib import Path

# Setup paths
core_dir = Path(__file__).parent.parent
sys.path.append(str(core_dir / "logic"))

try:
    from manager import SkillsManager
except ImportError as e:
    print(f"Error loading logic: {e}")
    sys.exit(1)

def main():
    # Detect repo root
    repo_root = Path(".").resolve()
    manager = SkillsManager(repo_root)
    
    parser = argparse.ArgumentParser(description="Third-party Skills Manager (Multi-provider)")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: find
    find_parser = subparsers.add_parser("find", help="Search for skills across providers")
    find_parser.add_argument("keywords", nargs="+", help="Keywords to search for")

    # Command: research
    research_parser = subparsers.add_parser("research", help="Deep analysis of candidates and local overlaps")
    research_parser.add_argument("keywords", nargs="+", help="Keywords to research")

    # Command: add
    add_parser = subparsers.add_parser("add", help="Install a skill from a specific provider")
    add_parser.add_argument("--provider", choices=manager.providers.keys(), default="skills.sh", help="Provider name")
    add_parser.add_argument("ref", help="Skill reference (e.g., owner/repo@skill or repo path)")

    args = parser.parse_args()

    if args.command == "find":
        print(manager.find_all(" ".join(args.keywords)))

    elif args.command == "research":
        analysis = manager.research_candidates(" ".join(args.keywords))
        print(manager.format_research_tables(analysis))
        if args.propose:
            print("\n--- Proposal Action ---")
            print(manager.propose_improvements(analysis))
    
    elif args.command == "add":
        print(f"Installing {args.ref} from {args.provider}...")
        print(manager.install_skill(args.provider, args.ref))

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
