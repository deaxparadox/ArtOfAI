from concurrent.futures import ProcessPoolExecutor
from numba import jit

from performance import timeit

@jit(nopython=True)
def __calculate_fibonacci(x: int) -> int:
    if x == 0:
        return 0
    if x == 1:
        return 1
    
    return __calculate_fibonacci(x-1) + __calculate_fibonacci(x-2)

@timeit
def factorial(x: int) -> None:
    value = __calculate_fibonacci(x)
    print(f"Factorial of {x} is {value}")
    


def main():
    nums = [
        40, 40, 40, 40
    ]
    # partials = [partial(factorial, x) for x in nums]
    with ProcessPoolExecutor() as executor:
        executor.map(factorial, nums)
    
    
if __name__ == "__main__":
    main()

