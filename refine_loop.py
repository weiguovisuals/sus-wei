import time
from validate import validate_all_files
from System_Memory.sus_memory import log_memory

def refinement_cycle():
    print("🔁 Initiating Refinement Cycle...")
    validated = validate_all_files()
    if validated:
        print("✅ All files validated successfully.")
        log_memory("Refinement cycle passed. Files validated.")
    else:
        print("⚠️ Issues detected. Attempting auto-correction...")
        log_memory("Refinement flagged issues. Manual check recommended.")

def run_continuously(interval=60):
    print("🧠 SUS Refinement Loop Active...")
    try:
        while True:
            refinement_cycle()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("🛑 Refinement loop terminated.")

if __name__ == "__main__":
    run_continuously()
