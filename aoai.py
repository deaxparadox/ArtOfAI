import os
import warnings
from pathlib import Path
from typing import Self



BASE_DIR = Path(__file__).parent

DATASET_DIR = os.path.join(BASE_DIR, "dataset")
DATASET_CLEAN_DIR = os.path.join(DATASET_DIR, "clean")

class Base:
    datasets = []
    
    def __init__(
        self, 
        base_dir = BASE_DIR, 
        dataset_dir = DATASET_DIR,
        dataset_clean_dir = DATASET_CLEAN_DIR
    ) -> None:
        self.__base_dir = base_dir
        self.__dataset_dir = dataset_dir,
        self.__dataset_clean_dir = dataset_clean_dir
        self.__load_dataset_path()
        
    def __load_dataset_path(self) -> None:
        for root, dirs, files in os.walk(DATASET_DIR):
            for file in files:
                self.datasets.append(os.path.join(root, file))
        return
    
    def refresh(self) -> None:
        # empty the `datasets` list
        self.datasets.clear()
        
        # reload the datasets
        self.__load_dataset_path()
        
        return None


class Find:
    # def __init__(self, obj: Base|None = None):
    #     self.__base = obj
        
    def __getitem__(self, name: str | list[str] | None = None) -> None:
        if not name:
            raise KeyError("find attribute name cannot be empty.")
        else:
            return getattr(self, name)
            
    def __call__(self, name: str | list[str] | None = None) -> str:
        if not name:
            raise KeyError("Invalid `name` values")
        try:
            for v in self.datasets:
                if self.__check_name(name, v):
                    return v
        except Exception as e:
            warnings.warn(e)
            
            

class Dataset(Base):
    def refresh(self) -> None:
        """
        Refresh the datasets.
        
        Load the datasets again.
        """
        super().refresh()
            
        
    def __check_name(self, name, path) -> bool:
        if name in path:
            return True
        return False


    def list_all(self, name: str | list[str] = None) -> str:
        """
        Print the list all the datasets.
        """
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
    
    def get(self, name: str | list[str] = None) -> list[str]:
        """
        Return the list all the datasets.
        """
        if not name:
            return self.datasets
        
        d = []
        
        # if name is `str`
        # return list of name
        if isinstance(name, str):
            for v in self.datasets:
                if self.__check_name(name, v):
                    d.append(v)
            
        # if name is list
        # return list of names
        if isinstance(name, list):
            for v in self.datasets:
                if all([self.__check_name(n, v) for n in name]):
                    d.append(v)
        
        return d
        
if __name__ == "__main__":
    ...