def __calculate_factrial(x: int) -> int:
    if x == 1:
        return 1
    return x * __calculate_factrial(x-1)

def factorial(x: int) -> None:
    value = __calculate_factrial(x)
    print(f"Factorial of {x} is {value}")
    
    
def main():
    factorial(40)
    
    
if __name__ == "__main__":
    main()

