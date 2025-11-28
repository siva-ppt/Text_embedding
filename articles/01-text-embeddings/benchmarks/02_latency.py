import time
from sentence_transformers import SentenceTransformer

def measure_latency(model_path, sample_text):
    model = SentenceTransformer(model_path)
    start_time = time.time()
    _ = model.encode(sample_text)
    return time.time() - start_time
