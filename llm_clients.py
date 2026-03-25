import os
import requests
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Fetch keys from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def call_fast_model(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    
    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    return f"Error: {result}"

def call_capable_model(prompt):
    # Note: Ensure the model name "gemini-2.5-flash" is correct for the current API version
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    data = {"contents": [{"parts": [{"text": prompt}]}]}

    response = requests.post(url, json=data)
    result = response.json()

    if "candidates" in result:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    return f"Error: {result}"