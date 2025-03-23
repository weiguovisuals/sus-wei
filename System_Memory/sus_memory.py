import json
from datetime import datetime
from pathlib import Path

MEMORY_FILE = Path("System_Memory/sus_memory.json")

def log_memory(entry: str):
    memory_entry = {
        "timestamp": datetime.now().isoformat(),
        "memory": entry
    }

    if not MEMORY_FILE.exists():
        MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(MEMORY_FILE, "w") as f:
            json.dump([memory_entry], f, indent=2)
    else:
        with open(MEMORY_FILE, "r+") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
            data.append(memory_entry)
            f.seek(0)
            json.dump(data, f, indent=2)
