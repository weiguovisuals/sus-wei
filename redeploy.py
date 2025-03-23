import os
import shutil
from pathlib import Path

# === CONFIGURATION ===
SUS_ROOT = Path.home() / "Documents" / "sus-wei"
BACKUP_ROOT = SUS_ROOT / "REDEPLOY"
EXCLUDE = ["__pycache__", ".DS_Store", "venv", "sus-wei-package.zip"]

# === HELPERS ===
def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def should_exclude(name):
    return any(excluded in name for excluded in EXCLUDE)

def copy_structure(src, dst):
    for root, dirs, files in os.walk(src):
        rel_root = Path(root).relative_to(src)
        target_root = dst / rel_root
        ensure_dir(target_root)

        for f in files:
            if should_exclude(f):
                continue
            src_file = Path(root) / f
            dst_file = target_root / f
            shutil.copy2(src_file, dst_file)

def create_deploy_readme(path):
    readme_path = path / "README_DEPLOY.md"
    with open(readme_path, "w") as f:
        f.write("# 🛠 SUS-Wei Redeployment Kit\n")
        f.write("- All scripts copied from ~/Documents/sus-wei\n")
        f.write("- Remove anything unused (e.g., logs, pycache)\n")
        f.write("- Run setup_sus_wei.py to initialize system\n")
    print("✅ README_DEPLOY.md created.")

# === MAIN ACTION ===
def generate_redeployment():
    if BACKUP_ROOT.exists():
        shutil.rmtree(BACKUP_ROOT)
    ensure_dir(BACKUP_ROOT)
    copy_structure(SUS_ROOT, BACKUP_ROOT)
    create_deploy_readme(BACKUP_ROOT)
    print(f"✅ Redeployment package created at: {BACKUP_ROOT}")

if __name__ == "__main__":
    generate_redeployment()