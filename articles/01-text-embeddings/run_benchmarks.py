import yaml
import os
from mteb import MTEB
from sentence_transformers import SentenceTransformer

# Load config
with open("benchmark_config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Define output directory
output_dir = "results/raw"

# Run benchmarks for each model
for model_info in config["models"]:
    model_name = model_info["name"]
    model_path = model_info["path"]
    print(f"Evaluating {model_name}...")

    # Load model with trust_remote_code=True
    model = SentenceTransformer(model_path, trust_remote_code=True)

    # Prepare MTEB evaluation
    evaluation = MTEB(tasks=config["tasks"])
    evaluation.run(
        model,
        output_folder=os.path.join(output_dir, model_name.replace("/", "_")),
        verbosity=2
    )
    print(f"Done with {model_name}\n")

print("All benchmarks completed.")
