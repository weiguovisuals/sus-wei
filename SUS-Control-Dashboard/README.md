# SUS-Control-Dashboard
- Memory Viewer
- Task Queue Display
- Trigger History

# 🧠 SUS Control Dashboard

A high-level control panel to manage execution logic, memory visualization, and live task refinement across the SUS-WEI system.

---

## 🧩 Modules

| Module Name        | Description                                           |
|--------------------|-------------------------------------------------------|
| Memory Viewer       | Displays current contents of `sus_memory.json`       |
| Task Queue Display  | Shows pending or active system tasks                 |
| Trigger History     | Logs all major invocations of system triggers        |
| Active Refinements  | Lists tools currently being improved/refined         |
| Git Sync Status     | Reflects git push/pull status dynamically            |
| Notion Sync Status  | Displays status of Notion logic transfer             |

---

## 🔁 System Hooks

- `/trigger.py` → Memory read/write
- `/sync_to_notion.py` → Push Markdown/Logic into Notion DB
- `/auto_sync.py` → Background sync to GitHub + Logs
- `/validate.py` → Health-check (Coming soon)
- `/setup_sus_wei.py` → System bootstrapper

---

## 🔍 Use Cases

- Monitor execution lifecycle across multiple tools
- Visualize memory evolution and logic snapshots
- Verify background sync status and auto-repair logic
