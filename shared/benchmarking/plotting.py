import matplotlib.pyplot as plt
import pandas as pd

def plot_metric_comparison(results_df, metric, title, output_file):
    """Plot metric comparison across models."""
    plt.figure(figsize=(10, 6))
    results_df.plot(x="Model", y=metric, kind="bar", title=title)
    plt.savefig(output_file)
    plt.close()
