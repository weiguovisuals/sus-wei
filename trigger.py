# SUS Memory Trigger Tool
import sys

if "--add-memory" in sys.argv:
    memory = sys.argv[sys.argv.index("--add-memory") + 1]
    with open("System_Memory/sus_memory.json", "a") as f:
        f.write(f'\n# Memory: {memory}\n')

elif "--add-task" in sys.argv:
    task = sys.argv[sys.argv.index("--add-task") + 1]
    with open("System_Memory/sus_tasks.json", "a") as f:
        f.write(f'\n- [ ] {task}\n')

elif "--refine" in sys.argv:
    tool = sys.argv[sys.argv.index("--refine") + 1]
    print(f"Refining tool: {tool} (placeholder logic)")

elif "--refine-all" in sys.argv:
    print("Refining all tools... (placeholder logic)")
