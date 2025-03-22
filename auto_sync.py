# Auto GitHub Sync Script
import subprocess

subprocess.run(["git", "add", "."], cwd=".")
subprocess.run(["git", "commit", "-m", "🔄 Auto-sync commit"], cwd=".")
subprocess.run(["git", "push", "origin", "main"], cwd=".")
print("✅ GitHub Sync Complete")
