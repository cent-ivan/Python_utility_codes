#can be use in Pascal's Triangle
def generate_fibonacci(length) -> None:
    print("Fibonacci Sequence")
    a = 0
    b = 1
    while a <= length:
        a, b = b, a + b
        print(a)


len = int(input("Enter length: "))
generate_fibonacci(len)