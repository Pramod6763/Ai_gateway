from fastapi import FastAPI
import time

from router_model import predict_route
from cache import get_cache, set_cache
from llm_clients import call_fast_model, call_capable_model
from logger import log_request

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/chat")
def chat(prompt: str):
    
    start = time.time()
    
    cached = get_cache(prompt)
    if cached:
        latency = time.time() - start
        log_request(prompt, "cache", "cache hit", latency, "hit")
        return {"response": cached, "cache": "hit"}
    
    model, confidence = predict_route(prompt)
    
    if model == "fast":
        response = call_fast_model(prompt)
    else:
        response = call_capable_model(prompt)
    
    set_cache(prompt, response)
    
    latency = time.time() - start
    
    log_request(prompt, model, f"confidence {confidence}", latency, "miss")
    
    return {
        "response": response,
        "model": model,
        "confidence": confidence,
        "latency": latency,
        "cache": "miss"
    }