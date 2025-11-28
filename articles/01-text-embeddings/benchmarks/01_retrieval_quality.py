from shared.benchmarking.metrics import load_results
from shared.benchmarking.reporting import export_results_to_csv

def evaluate_retrieval_quality(model_folders):
    results = []
    for folder in model_folders:
        data = load_results(folder)
        if data:
            # Extract retrieval metrics (example: MRR, MAP)
            mrr = data.get("retrieval", {}).get("MRR", None)
            results.append({"Model": os.path.basename(folder), "MRR": mrr})
    export_results_to_csv(results, "results/processed/retrieval_quality.csv")
