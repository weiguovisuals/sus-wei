import os
from pathlib import Path
from datetime import datetime

# Define key files and paths to validate
VALIDATION_TARGETS = [
    "trigger.py",
    "sync_to_notion.py",
    "auto_sync.py",
    "redeploy.py",
    "setup_sus_wei.py",
    "System_Memory/sus_memory.json",
    "Refinement_Logs/cycle_summary.log",
    "SUS-Control-Dashboard/README.md",
    "sus_blueprint.md",
    "SUS-REDEPLOY.md",
    "execution_flow.md",
]

def log_result(path, exists):
    status = "✅ EXISTS" if exists else "❌ MISSING"
    print(f"{status}: {path}")
    return f"{status}: {path}"

def run_validation():
    base_path = Path(__file__).resolve().parent
    results = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n📋 VALIDATION REPORT — {timestamp}\n{'-' * 50}")
    results.append(f"\n[Validation Timestamp: {timestamp}]")

    for target in VALIDATION_TARGETS:
        full_path = base_path / target
        exists = full_path.exists()
        results.append(log_result(target, exists))

    log_path = base_path / "Refinement_Logs" / "cycle_summary.log"
    log_path.parent.mkdir(exist_ok=True, parents=True)
    with open(log_path, "a") as f:
        f.write("\n".join(results) + "\n")

    print("\n📦 Validation logged to cycle_summary.log")

if __name__ == "__main__":
    run_validation()
def validate_all_files():
    required_files = [
        "trigger.py", "auto_sync.py", "sync_to_notion.py",
        "redeploy.py", "setup_sus_wei.py", "validate.py",
        "System_Memory/sus_memory.json", "Refinement_Logs/cycle_summary.log",
        "SUS-Control-Dashboard/README.md", "sus_blueprint.md",
        "SUS-REDEPLOY.md", "execution_flow.md"
    ]
    all_valid = True
    for f in required_files:
        if not os.path.exists(f):
            print(f"❌ MISSING: {f}")
            all_valid = False
    return all_valid
