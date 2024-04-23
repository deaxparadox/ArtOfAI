import os
import warnings

def get_dataset(name: str) -> str:
    dataset_path = os.environ.get("ARTOFAIDATASET", None)
    if not dataset_path:
        warnings.warn("Dataset environment not set.")
        