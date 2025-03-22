import time
import threading

def run_simulated_task(task_id):
    print(f"Starting task {task_id}")
    time.sleep(1)
    print(f"Completed task {task_id}")

def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=run_simulated_task, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
