import os
import json
import sys
from datetime import datetime

# === CONFIG ===
BASE_PATH = os.path.expanduser("~/Documents/sus-wei")
MEMORY_PATH = os.path.join(BASE_PATH, "System_Memory/sus_memory.json")
LOG_PATH = os.path.join(BASE_PATH, "Refinement_Logs/cycle_summary.log")

# === HELPERS ===
def load_memory():
    if not os.path.exists(MEMORY_PATH):
        return []
    with open(MEMORY_PATH, "r") as f:
        return json.load(f)

def save_memory(mem_list):
    os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
    with open(MEMORY_PATH, "w") as f:
        json.dump(mem_list, f, indent=2)

def append_log(entry):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {entry}\n")

# === COMMANDS ===
def add_memory(entry):
    mem_list = load_memory()
    mem_list.append(f"# Memory: {entry}")
    save_memory(mem_list)
    append_log(f"🧠 Memory added: {entry}")
    print(f"✅ Memory updated.")

def show_memory():
    mem_list = load_memory()
    print("🧠 MEMORY SNAPSHOT:\n")
    for m in mem_list:
        print(m)

def show_status():
    show_memory()
    print("\n📋 TASK QUEUE:")
    print("❌ No task queue found.")  # Placeholder for task integration

def usage():
    print("Usage:")
    print("  python3 trigger.py --add-memory \"Your memory item here\"")
    print("  python3 trigger.py --status")

# === MAIN ===
if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    if sys.argv[1] == "--add-memory" and len(sys.argv) >= 3:
        add_memory(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "--status":
        show_status()
    else:
        print("❌ Unknown command.")
        usage()