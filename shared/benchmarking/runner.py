import yaml
from mteb import MTEB
from sentence_transformers import SentenceTransformer

def run_model_benchmark(model_path, tasks, output_folder):
    model = SentenceTransformer(model_path)
    evaluation = MTEB(tasks=tasks)
    results = evaluation.run(model, output_folder=output_folder)
    return results
