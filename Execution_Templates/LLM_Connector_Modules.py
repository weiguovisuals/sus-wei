import requests

def call_gpt(prompt):
    response = requests.post("https://api.openai.com/v1/chat/completions", json={
        "model": "gpt-4",
        "messages": [{"role": "user", "content": prompt}]
    }, headers={"Authorization": "Bearer YOUR_API_KEY"})
    return response.json()
