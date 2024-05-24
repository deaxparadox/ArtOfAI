from performance import timeit


def __calculate_fibonacci(x: int) -> int:
    if x == 0:
        return 0
    if x == 1:
        return 1
    
    return __calculate_fibonacci(x-1) + __calculate_fibonacci(x-2)

@timeit
def fibonacci(x: int) -> None:
    value = __calculate_fibonacci(x)
    print(f"Factorial of {x} is {value}")
    

def main():
    fibonacci(40)
    
    
if __name__ == "__main__":
    main()

