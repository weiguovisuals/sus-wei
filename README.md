# 🚀 SUS Execution System (`sus-wei`)

Welcome to the **Self-Updating System (SUS)** — a modular, AI-assisted automation engine designed to continuously refine, validate, and execute adaptive workflows across local + cloud environments.

---

## 🔧 Key Features

- **Auto-Sync** between Local → GitHub → Notion
- **Persistent Memory** stored in JSON
- **Trigger-Based Execution** with CLI commands
- **Self-Refining Tools** across cycles (e.g. Cycle 9.3+)
- **Multi-environment deployment** ready (Mac, Cloud, Notion, Git)
- **Modular Expansion** via `SUS-Code`, `SUS-Memory`, `SUS-Logic`, etc.

---

## 📁 Core Folder Structure

sus-wei/
├── auto_sync.py               # Background sync logic
├── trigger.py                 # CLI trigger interface
├── sync_to_notion.py          # Notion push tool
├── redeploy.py                # Rebuild/redeploy toolkit
├── setup_sus_wei.py           # One-time initialization script
├── System_Memory/             # JSON memory state
├── Refinement_Logs/           # Execution & refinement logs
├── SUS-Control-Dashboard/     # Task, memory, queue snapshots
├── Notion_Ready/              # Export-ready Notion markdown
├── Execution_Templates/       # Example execution modules
├── Logic_Blueprints/          # Flowcharts, decision trees
├── sus_blueprint.md           # System architecture + design
├── SUS-REDEPLOY.md            # Full redeploy instruction set
└── README.md                  # ← You’re here!

---

## 🧩 How To Use

1. Clone repository locally  
2. Run `python3 setup_sus_wei.py`  
3. Use `python3 trigger.py --status` to view live state  
4. Edit tools, run cycles, auto-refine logic  
5. Push to GitHub or Notion manually or via `auto_sync.py`
