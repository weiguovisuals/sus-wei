import os
import sys
import json
from datetime import datetime

MEMORY_FILE = "System_Memory/sus_memory.json"
QUEUE_FILE = "System_Memory/task_queue.json"
LOG_FILE = "Refinement_Logs/trigger_history.log"

def add_memory(entry):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    try:
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        memory = []

    memory.append({"timestamp": datetime.now().isoformat(), "memory": entry})
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def add_task(task):
    os.makedirs(os.path.dirname(QUEUE_FILE), exist_ok=True)
    try:
        with open(QUEUE_FILE, "r") as f:
            queue = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        queue = []

    queue.append({"timestamp": datetime.now().isoformat(), "task": task})
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

def log_trigger(action):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {action}\n")

def refine(tool):
    log_trigger(f"Refinement requested for tool: {tool}")
    print(f"🔧 Refining logic for {tool}... (placeholder logic)")

def view_status():
    print("🧠 MEMORY SNAPSHOT:")
    try:
        with open(MEMORY_FILE, "r") as f:
            print(f.read())
    except:
        print("❌ No memory log found.")

    print("\n📋 TASK QUEUE:")
    try:
        with open(QUEUE_FILE, "r") as f:
            print(f.read())
    except:
        print("❌ No task queue found.")

if __name__ == "__main__":
    if len(sys.argv) < 3 and sys.argv[1] != "--status":
        print("Usage:")
        print("  python3 trigger.py --add-memory \"<entry>\"")
        print("  python3 trigger.py --add-task \"<task>\"")
        print("  python3 trigger.py --refine \"<tool_name>\"")
        print("  python3 trigger.py --status")
        sys.exit(1)

    cmd, arg = sys.argv[1], " ".join(sys.argv[2:])
    if cmd == "--add-memory":
        add_memory(arg)
        log_trigger(f"Added memory: {arg}")
    elif cmd == "--add-task":
        add_task(arg)
        log_trigger(f"Added task: {arg}")
    elif cmd == "--refine":
        refine(arg)
    elif cmd == "--status":
        view_status()
    else:
        print("❌ Unknown command.")