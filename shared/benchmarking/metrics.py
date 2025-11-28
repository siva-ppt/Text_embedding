import json
import os

def load_results(model_folder):
    """Load MTEB results from JSON."""
    json_path = os.path.join(model_folder, "results.json")
    if not os.path.isfile(json_path):
        return None
    with open(json_path, "r") as f:
        return json.load(f)
