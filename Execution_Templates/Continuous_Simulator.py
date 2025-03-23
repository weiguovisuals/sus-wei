import time
import random

class ContinuousExecutionSimulator:
    def __init__(self):
        self.state = "IDLE"
        self.memory_trigger = []
        self.cycle_count = 0

    def simulate_cycle(self):
        self.state = "EXECUTING"
        print(f"🔁 Running execution cycle #{self.cycle_count + 1}")
        duration = random.uniform(0.5, 2.0)
        time.sleep(duration)
        print(f"✅ Cycle complete in {round(duration, 2)}s")
        self.memory_trigger.append(f"Cycle {self.cycle_count + 1} complete")
        self.cycle_count += 1

    def run_forever(self, limit=5):
        print("🧠 Continuous Execution Simulator Started...")
        while self.cycle_count < limit:
            self.simulate_cycle()
        self.state = "COMPLETE"
        print("🛑 Execution Simulator Finished.")

if __name__ == "__main__":
    sim = ContinuousExecutionSimulator()
    sim.run_forever()