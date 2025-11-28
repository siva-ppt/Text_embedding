def estimate_cost(model_size, num_samples, cost_per_token=0.0001):
    """Estimate inference cost based on model size and sample count."""
    return model_size * num_samples * cost_per_token
