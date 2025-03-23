import os
import subprocess
from pathlib import Path

def create_structure(base_dir):
    print(f"🛠 Setting up SUS-WEI structure in {base_dir}")
    dirs = [
        "System_Memory",
        "Refinement_Logs",
        "Execution_Templates",
        "Notion_Ready",
        "Logic_Blueprints",
        "REDEPLOY",
        "SUS-Control-Dashboard",
    ]
    files = [
        "trigger.py",
        "auto_sync.py",
        "sync_to_notion.py",
        "redeploy.py",
        "sus_blueprint.md",
        "SUS-REDEPLOY.md",
        "execution_flow.md",
        "README.md"
    ]

    for d in dirs:
        Path(base_dir, d).mkdir(parents=True, exist_ok=True)
        print(f"📁 Created directory: {d}")

    for f in files:
        file_path = Path(base_dir, f)
        if not file_path.exists():
            file_path.touch()
            print(f"📄 Created placeholder file: {f}")
        else:
            print(f"✅ File already exists: {f}")

def install_dependencies():
    print("📦 Installing core dependencies...")
    try:
        subprocess.run(["pip3", "install", "-r", "requirements.txt"], check=True)
    except Exception as e:
        print(f"⚠️ Error installing dependencies: {e}")

def main():
    base_dir = str(Path(__file__).resolve().parent)
    create_structure(base_dir)
    install_dependencies()
    print("✅ SUS-WEI setup complete.")

if __name__ == "__main__":
    main()