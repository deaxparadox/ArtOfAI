import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f"Total time: {time.time() - start}")
        return
    return wrapper
