# ✅ execution_flow.md

# ⚙️ SUS SYSTEM EXECUTION FLOW

This file outlines the **core execution pathway** of the SUS (Self-Updating System) architecture, showing how tasks, memory, validation, and refinement interact dynamically.

---

## 📌 OVERVIEW

The SUS system uses modular Python scripts to process tasks, generate memory blocks, validate system integrity, and run iterative self-improvement loops.

Each module acts as a node in a live decision-making framework, continuously syncing files, logs, and logic states for long-term retraining or scaling.

---

## 🔁 SYSTEM EXECUTION LOOP

┌──────────────┐
│  User Input  │
└──────┬───────┘
       │
       ▼
┌──────────────────────┐
│  trigger.py          │ ← Accepts input or memory instruction
└────────┬─────────────┘
         │ writes to memory/tasks
         ▼
┌──────────────────────┐
│  validate.py         │ ← Validates core file structure
└────────┬─────────────┘
         │ triggers auto-fixes if needed
         ▼
┌──────────────────────┐
│  refine_loop.py      │ ← Runs logic correction & optimization
└────────┬─────────────┘
         │ looped on every cycle
         ▼
┌──────────────────────┐
│  sync_to_notion.py   │ ← Syncs logs/docs to Notion or iCloud
└────────┬─────────────┘
         │
         ▼
┌──────────────────────┐
│  auto_sync.py        │ ← Optional: schedules syncing jobs
└────────┬─────────────┘
         ▼
┌──────────────────────────────┐
│  Continuous_Simulator.py     │ ← (Optional) Runs system-wide prediction loop
└──────────────────────────────┘

---

## 🔄 ACTIVE MODULE DEPENDENCIES

| Module                  | Triggered By              | Writes To                           |
|------------------------|---------------------------|--------------------------------------|
| `trigger.py`           | Manual input / CLI        | `sus_memory.json`, `sus_tasks.json` |
| `validate.py`          | Any trigger or startup    | Logs + validation + creates files   |
| `refine_loop.py`       | Looped via CLI or sim     | `cycle_summary.log`, memory         |
| `sync_to_notion.py`    | Manual/auto               | iCloud or Notion                    |
| `auto_sync.py`         | Timed event               | Sync trigger every X mins           |
| `redeploy.py`          | Manual/cron               | Resets or rebuilds files            |
| `setup_sus_wei.py`     | One-time setup            | Initializes folders + logic stubs   |

---

## 🧠 MEMORY-DRIVEN PATHWAYS

Memory files like `sus_memory.json` and `sus_tasks.json` are dynamically updated by every cycle. They also **inform future logic generation**, `refine_loop.py`, and AI execution suggestions.

```json
{
  "last_trigger": "Refine execution_flow.md and sync with system logs",
  "last_validated": "2025-03-23T05:29",
  "pending_tasks": ["Push execution_flow.md", "Add to training payload"]
}



⸻

🧩 SIMULATION & FUTURE VECTORS

If active, Continuous_Simulator.py tracks and simulates the following:
	•	📊 Refinement patterns across sessions
	•	🔁 Looped corrections of logic over time
	•	🔮 Predictive memory formation and anomaly recovery

⸻

🧰 EXECUTION INSTRUCTIONS

To manually trigger a full system execution loop:

cd ~/Documents/sus-wei

python3 trigger.py "Refine SUS architecture"
python3 validate.py
python3 refine_loop.py
python3 sync_to_notion.py

To launch a full redeployment or reset:

sh deploy_sus.sh



⸻

🧠 PERSISTENT SYSTEM STATE

Every loop appends to cycle_summary.log, which provides history for retraining:

[CYCLE 9.3]
- Refined tool_docs.md
- Validated memory
- Populated execution_flow.md
- Auto-pushed to GitHub



⸻

✅ FINAL STATUS

This file (execution_flow.md) has been regenerated with fully validated content, designed to:
	•	Guide human/AI users through SUS system behavior
	•	Train or fine-tune new LLMs on execution patterns
	•	Serve as a retraining module in future SUS variants

🟢 Ready for copy-paste and deployment.

