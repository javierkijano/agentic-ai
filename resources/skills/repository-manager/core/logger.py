import datetime
import os
import pathlib

def get_log_path():
    # Resolver la raíz del repo desde este archivo
    # core/logger.py -> repository-manager/core/logger.py
    repo_root = pathlib.Path(__file__).parent.parent.parent.parent.parent
    
    # Contexto por defecto: gemini-cli (ya que soy yo quien lo usa ahora)
    # En el futuro esto puede venir de una variable de entorno
    context = os.environ.get("AGENTIC_CONTEXT", "gemini-cli")
    
    log_dir = repo_root / "runtime" / context / "repository-manager" / "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    return log_dir / "repository.log"

def log_operation(operation, status, details=""):
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"[{timestamp}] OP: {operation} | STATUS: {status} | DETAILS: {details}\n"
    
    log_file = get_log_path()
    
    with open(log_file, "a") as f:
        f.write(log_entry)
