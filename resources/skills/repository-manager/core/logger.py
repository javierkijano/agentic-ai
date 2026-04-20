import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "../../../../shared/logs/repository.log")

def log_operation(operation, status, details=""):
    timestamp = datetime.datetime.now().isoformat()
    log_entry = f"[{timestamp}] OP: {operation} | STATUS: {status} | DETAILS: {details}\n"
    
    # Asegurar que el directorio existe (por si acaso)
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)
