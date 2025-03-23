import os
import subprocess
import time
from datetime import datetime

# Paths
BASE_PATH = os.path.expanduser("~/Documents/sus-wei")
GIT_COMMIT_MESSAGE = "🔁 Auto-sync: Real files + memory + logic updates"

def git_push():
    try:
        subprocess.run(["git", "add", "."], cwd=BASE_PATH, check=True)
        subprocess.run(["git", "commit", "-m", GIT_COMMIT_MESSAGE], cwd=BASE_PATH, check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_PATH, check=True)
        print(f"✅ Git auto-sync complete at {datetime.now()}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git sync failed: {e}")

def background_sync_loop(interval=1800):
    print("🔁 Starting background auto-sync loop...")
    while True:
        git_push()
        time.sleep(interval)

if __name__ == "__main__":
    background_sync_loop(1800)  # 30 minutes