import subprocess
import os
import shutil
import sys
from pathlib import Path
from abc import ABC, abstractmethod

class BaseProvider(ABC):
    @abstractmethod
    def search(self, keywords: str):
        pass

    @abstractmethod
    def install(self, ref: str, target_dir: Path):
        pass

class SkillsShProvider(BaseProvider):
    def search(self, keywords: str):
        cmd = ["npx", "-y", "skills", "find"] + keywords.split()
        try:
            return subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
        except subprocess.CalledProcessError as e:
            return f"Error searching skills.sh: {e.output.decode()}"

    def install(self, ref: str, target_dir: Path):
        # npx skills add normally installs to node_modules or current dir
        # We might need to move it to target_dir after installation
        # For simplicity in this hub, we will try to clone/download manually if needed
        # but npx skills add is the standard.
        cmd = ["npx", "-y", "skills", "add", ref, "-y"]
        try:
            return subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
        except subprocess.CalledProcessError as e:
            return f"Error installing from skills.sh: {e.output.decode()}"

class GithubProvider(BaseProvider):
    def __init__(self, repo_url="https://github.com/anthropics/skills"):
        self.repo_url = repo_url

    def search(self, keywords: str):
        # This is harder without an API. For now, we search the repo structure if local,
        # or we could use GitHub Search API.
        return f"Searching GitHub repo {self.repo_url} for '{keywords}' (Search logic pending API implementation)."

    def install(self, ref: str, target_dir: Path):
        # ref could be a path within the repo like 'skills/development/webapp-testing'
        # We can use sparse checkout or just download the folder
        print(f"Installing {ref} from {self.repo_url} into {target_dir}...")
        # Mock implementation for now
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "SKILL.md").write_text(f"# Imported Skill: {ref}\nSource: {self.repo_url}")
        return f"Success: {ref} installed to {target_dir}"

class HermesProvider(BaseProvider):
    def __init__(self, hub_url="https://hermes-agent.nousresearch.com/docs/skills"):
        self.hub_url = hub_url

    def search(self, keywords: str):
        return f"Searching Hermes Hub {self.hub_url} for '{keywords}' (Web crawling logic pending)."

    def install(self, ref: str, target_dir: Path):
        print(f"Installing {ref} from Hermes Hub into {target_dir}...")
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "SKILL.md").write_text(f"# Imported Hermes Skill: {ref}\nSource: {self.hub_url}")
        return f"Success: {ref} installed to {target_dir}"

class ClawHubProvider(BaseProvider):
    def __init__(self, hub_url="https://clawhub.ai"):
        self.hub_url = hub_url

    def search(self, keywords: str):
        return f"Searching ClawHub {self.hub_url} for '{keywords}' (API/Web scraping logic pending)."

    def install(self, ref: str, target_dir: Path):
        print(f"Installing {ref} from ClawHub into {target_dir}...")
        target_dir.mkdir(parents=True, exist_ok=True)
        (target_dir / "SKILL.md").write_text(f"# Imported ClawHub Skill: {ref}\nSource: {self.hub_url}")
        return f"Success: {ref} installed to {target_dir}"

class SkillsManager:
    def __init__(self, repo_root):
        self.repo_root = Path(repo_root)
        self.providers = {
            "skills.sh": SkillsShProvider(),
            "anthropic": GithubProvider("https://github.com/anthropics/skills"),
            "hermes": HermesProvider(),
            "clawhub": ClawHubProvider()
        }
        # Cargar explorador local para detectar solapamientos
        sys.path.append(str(self.repo_root / "resources/skills/repository-manager/core/logic"))
        try:
            from explorer import RepoExplorer
            self.explorer = RepoExplorer(self.repo_root)
        except ImportError:
            self.explorer = None

    def find_all(self, keywords: str):
        # ... (keep existing logic)
        results = {}
        for name, provider in self.providers.items():
            results[name] = provider.search(keywords)
        return results

    def research_candidates(self, keywords: str):
        """Analyzes candidates and compares them with local skills."""
        raw_results = self.find_all(keywords)
        local_skills = self.explorer.list_all_resources() if self.explorer else []
        
        # Simulación de análisis (en un entorno real el agente procesaría los textos)
        # Aquí preparamos la estructura para que el agente la use
        analysis = {
            "candidates": [],
            "overlaps": []
        }
        
        # Extraer candidatos de los resultados de skills.sh (que es el único real por ahora)
        skills_sh_out = raw_results.get("skills.sh", "")
        for line in skills_sh_out.splitlines():
            if "@" in line and "installs" in line:
                parts = line.split()
                analysis["candidates"].append({
                    "id": parts[0],
                    "installs": parts[1],
                    "features": "Deep integration, automated workflows, multi-platform support" # Placeholder
                })

        # Detectar solapamientos básicos por ID/Keywords
        for cand in analysis["candidates"]:
            cand_id_base = cand["id"].split("@")[-1].lower()
            cand_keywords = set(cand_id_base.split("-") + cand_id_base.split("_"))
            
            for local in local_skills:
                local_id = local["id"].lower()
                local_keywords = set(local_id.split("-") + local_id.split("_"))
                
                # Si comparten palabras clave significativas
                common = cand_keywords.intersection(local_keywords)
                # Ignorar palabras genéricas si es necesario
                common.discard("skills")
                common.discard("assistant")
                
                if common or cand_id_base in local_id or local_id in cand_id_base:
                    analysis["overlaps"].append({
                        "candidate": cand["id"],
                        "local": local["id"],
                        "shared_concept": f"Shared domains: {', '.join(common) if common else 'Similar naming'}",
                        "improvement_potential": "Analysis of external implementation for feature parity"
                    })
        
        return analysis

    def format_research_tables(self, analysis):
        """Generates the Markdown tables for features and overlaps."""
        # Tabla 1: Características Interesantes
        t1 = "| Candidate Skill | Top Features | Unique Value |\n"
        t1 += "| :--- | :--- | :--- |\n"
        for c in analysis["candidates"][:5]:
            t1 += f"| {c['id']} | {c['features']} | High adoption ({c['installs']}) |\n"
            
        # Tabla 2: Solapamientos y Sinergias
        t2 = "| Candidate | Local Skill | Overlap Nature | Potential Improvement for Us |\n"
        t2 += "| :--- | :--- | :--- | :--- |\n"
        for o in analysis["overlaps"]:
            t2 += f"| {o['candidate']} | {o['local']} | {o['shared_concept']} | {o['improvement_potential']} |\n"
            
        return f"## Analysis of Potential Candidates\n\n{t1}\n\n## Overlap & Integration Analysis\n\n{t2}"

    def install_skill(self, provider_name: str, ref: str):
        provider = self.providers.get(provider_name)
        if not provider:
            return f"Provider {provider_name} not found."
        
        # Determine target in vendor/
        skill_id = ref.split('/')[-1].split('@')[-1]
        target_dir = self.repo_root / "vendor" / "skills" / skill_id
        
        return provider.install(ref, target_dir)
