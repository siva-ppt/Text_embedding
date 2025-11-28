import pandas as pd
import json
import os

def export_results_to_csv(results_dict, output_file):
    """Export results to CSV."""
    df = pd.DataFrame(results_dict)
    df.to_csv(output_file, index=False)

def export_results_to_json(results_dict, output_file):
    """Export results to JSON."""
    with open(output_file, "w") as f:
        json.dump(results_dict, f, indent=4)
