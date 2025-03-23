import openai
import json

class LLMConnector:
    def __init__(self, model="gpt-4"):
        self.model = model
        self.history = []

    def query(self, prompt: str, temperature: float = 0.5) -> str:
        self.history.append(prompt)
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature
            )
            result = response['choices'][0]['message']['content']
            self.history.append(result)
            return result.strip()
        except Exception as e:
            return f"[LLMConnector Error]: {str(e)}"

    def save_history(self, path="llm_history.json"):
        with open(path, "w") as f:
            json.dump(self.history, f, indent=2)

    def clear_history(self):
        self.history = []