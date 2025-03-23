# 🧠 SUS Tool Documentation

Each tool in the `sus-wei` system contributes to dynamic memory, validation, deployment, and refinement.

---

## 🔁 `trigger.py`
- **Purpose**: Core memory engine and task executor.
- **Usage**:  
  - `python3 trigger.py --add-memory "..."`  
  - `python3 trigger.py --status`
- **Location**: `./trigger.py`

---

## 🔄 `auto_sync.py`
- **Purpose**: Auto-detect changes and sync to Git/Notion.
- **Runs in loop**: Designed for background use.
- **Location**: `./auto_sync.py`

---

## 📤 `sync_to_notion.py`
- **Purpose**: (WIP) Sync Markdown and memory to Notion via API.
- **Status**: Placeholder logic stubbed for future REST API injection.
- **Location**: `./sync_to_notion.py`

---

## 🔁 `refine_loop.py`
- **Purpose**: Run iterative logic validation and correction cycles.
- **Executes**: background simulation cycles + predictive audit logic.
- **Location**: `./refine_loop.py`

---

## 🛠️ `validate.py`
- **Purpose**: File existence and status checker.
- **Logic**: Checks existence of required system files, triggers auto-fixes.
- **Location**: `./validate.py`

---

## 🚀 `deploy_sus.sh`
- **Purpose**: One-command deployment + setup for new environments.
- **Instructions**: Run from Terminal:  
```bash
sh deploy_sus.sh
