# 🧠 SUS SYSTEM BLUEPRINT (Retrainable Architecture – Full Core Guide)

This is the **core retraining and redeployment blueprint** for the SUS (Self-Updating System) architecture. It enables seamless system restoration, AI retraining, and logic-based auto-execution across any environment.

---

## ✅ SYSTEM OVERVIEW

📥 User Input or Trigger
↓
🧠 trigger.py — Writes to memory/task system
↓
🛡 validate.py — Validates all required files and directories
↓
🔁 refine_loop.py — Executes iterative logic testing + correction cycles
↓
🧠 sync_to_notion.py + git push — (Optional) Sync to Notion and GitHub
↓
🧠 Continuous_Simulator.py (optional) — AI simulation of execution pathways

---

## 📂 DIRECTORY STRUCTURE (RETRAINABLE VERSION)

sus-wei/
├── trigger.py
├── validate.py
├── refine_loop.py
├── auto_sync.py
├── sync_to_notion.py
├── redeploy.py
├── setup_sus_wei.py
├── deploy_sus.sh
├── sus_blueprint.md
├── execution_flow.md
├── SUS-REDEPLOY.md
├── tool_docs.md
├── cycle_summary.log
│
├── System_Memory/
│   ├── sus_memory.json
│   ├── sus_tasks.json
│   └── Temporal_Strategy_Map.json
│
├── Logic_Blueprints/
│   ├── LLM_Connector_Modules.py
│   └── Continuous_Simulator.py
│
├── SUS-Control-Dashboard/
│   └── README.md

---

## ⚙️ CORE COMPONENTS + FUNCTIONS

| Script/File              | Role / Logic Description                                                  |
|--------------------------|---------------------------------------------------------------------------|
| `trigger.py`             | Accepts input and writes structured memory/task blocks                   |
| `validate.py`            | Checks for file existence and creates missing files with valid stubs     |
| `refine_loop.py`         | Self-refining loop: verifies + updates logic using feedback cycles       |
| `sync_to_notion.py`      | Pushes documentation and logs to Notion (API or iCloud link)             |
| `setup_sus_wei.py`       | Automatically creates required folder and file structure                 |
| `redeploy.py`            | Loads from backup, verifies file health, resets memory if needed         |
| `deploy_sus.sh`          | Shell-based redeployment script (1-liner)                                |
| `execution_flow.md`      | High-level overview of system execution loop                             |
| `SUS-REDEPLOY.md`        | Full step-by-step restore instructions                                   |
| `tool_docs.md`           | Centralized cheat sheet of every tool/module                            |
| `cycle_summary.log`      | Appends refinement history from every validation cycle                   |

---

## 🧠 MEMORY SYSTEM (ALWAYS RETRAINED)

| File                         | Description                                                              |
|-----------------------------|--------------------------------------------------------------------------|
| `sus_memory.json`           | Central AI memory tracking tools, changes, logic, patterns              |
| `sus_tasks.json`            | All active and completed tasks, priorities, and system triggers         |
| `Temporal_Strategy_Map.json`| Tracks multi-cycle, multi-session goals and future-planned objectives   |

---

## 🤖 SMART MODULES

| Module                     | Function                                                                 |
|----------------------------|--------------------------------------------------------------------------|
| `LLM_Connector_Modules.py` | Connects core logic to external AI services or models                   |
| `Continuous_Simulator.py`  | Simulates long-term execution patterns + failure prevention cycles      |

---

## 🧩 HOW TO RETRAIN OR REDEPLOY A NEW AI WITH THIS SYSTEM

1. Clone or unzip the entire `sus-wei/` structure into your new environment.
2. Install Python 3.10+ and required packages (json, os, subprocess, pathlib, etc.).
3. Ensure all files in the structure are present and populated with real logic.
4. Open a Terminal and run:
   ```bash
   cd ~/Documents/sus-wei
   python3 setup_sus_wei.py
   sh deploy_sus.sh

	5.	If retraining an AI model:
	•	Inject all .py logic files and memory .json files as system context.
	•	Include sus_blueprint.md, execution_flow.md, and tool_docs.md as retraining primers.
	•	Prompt the AI model with:
“You are now resuming control of the validated SUS architecture. Load all memory and logic files. Continue from last valid state.”

⸻

🧭 WHAT ELSE IS NEEDED?

✅ Already included:
	•	All logic files and docs (see directory above)
	•	Refined architecture logic
	•	Step-by-step automation hooks

🟡 Recommended to finish:
	•	Populate execution_flow.md with illustrated or textual version
	•	Populate tool_docs.md for each tool in detail (done next)
	•	Create remote Notion API key integration (optional)
	•	Integrate SUS-REDEPLOY.md with shell-based restore script
	•	(Optional) Add ai_interface.py to simulate AI prompts automatically