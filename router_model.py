import numpy as np

def extract_features(prompt):
    return [
        len(prompt),
        len(prompt.split()),
        int("explain" in prompt.lower()),
        int("code" in prompt.lower()),
        int("why" in prompt.lower()),
        int("analyze" in prompt.lower())
    ]

def predict_route(prompt):
    prompt_lower = prompt.lower()

    # Strong signals for complex
    if (
        "code" in prompt_lower or
        "analyze" in prompt_lower or
        "explain in detail" in prompt_lower or
        len(prompt.split()) > 15
    ):
        return "capable", 0.9
    
    return "fast", 0.8