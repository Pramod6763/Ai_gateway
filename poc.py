import json
from router_model import predict_route

with open("test_prompts.json") as f:
    data = json.load(f)

correct = 0
false_positive = 0
false_negative = 0

for item in data:
    pred, conf = predict_route(item["prompt"])
    actual = item["label"]

    if pred == actual:
        correct += 1
    elif pred == "fast" and actual == "capable":
        false_negative += 1
    elif pred == "capable" and actual == "fast":
        false_positive += 1

    print(f"\nPrompt: {item['prompt']}")
    print(f"Predicted: {pred}, Actual: {actual}, Confidence: {conf}")

total = len(data)

print("\n--- SUMMARY ---")
print("Accuracy:", correct/total)
print("False Positives:", false_positive)
print("False Negatives:", false_negative)