import json
import numpy as np

def analyze_metrics(file_path):
    with open(file_path) as f:
        data = json.load(f)

    durations = [entry["duration"] for entry in data if entry["status"] == "success"]
    p95 = np.percentile(durations, 95)
    p99 = np.percentile(durations, 99)
    success_rate = len(durations) / len(data)

    print(f"P95: {p95:.4f}s")
    print(f"P99: {p99:.4f}s")
    print(f"Success Rate: {success_rate * 100:.2f}%")

analyze_metrics("results.json")