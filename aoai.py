import os
import warnings
from pathlib import Path



BASE_DIR = Path(__file__).parent

DATASET_DIR = os.path.join(BASE_DIR, "dataset")


class Base:
    datasets = []


class Find:
    def __init__(self, datasets: list[str] | None = None) -> None:
        if not datasets:
            warnings.User
        
    def __getitem__(self, name: str | None = None) -> None:
        if not name:
            raise KeyError("find attribute name cannot be empty.")
        else:
            return getattr(self, name)
            
    def __call__(self, name: str | None = None) -> str:
        if not name:
            raise KeyError("Invalid `name` values")
        try:
            for v in self.datasets:
                if self.__check_name(name, v):
                    return v
        except Exception as e:
            warnings.warn(e)

class Dataset:
    datasets = []
    
    def __init__(self, base_dir = BASE_DIR, dataset_dir = DATASET_DIR) -> None:
        self.__base_dir = base_dir
        self.__dataset_dir = dataset_dir
        self.find = Find()
        
        
        self.__load_dataset_path()
    
    def __load_dataset_path(self) -> None:
        count = 1
        for root, dirs, files in os.walk(DATASET_DIR):
            for file in files:
                self.datasets.append(os.path.join(root, file))
        return
        



    def get_dataset(self) -> str:
        return
            
        
    def __check_name(self, name, path) -> bool:
        if name in path:
            return True
        return False


    def list_dataset(self, name: str | list[str] = None) -> str:
        if name:
            if isinstance(name, str):
                
                for v in self.datasets:
                    if self.__check_name(name, v):
                        print(v)
            if isinstance(name, list):
                # check all names
                for v in self.datasets:
                    if all([self.__check_name(n, v) for n in name]):
                        print(v)
        else:
            for v in self.datasets:
                print(v)
        return