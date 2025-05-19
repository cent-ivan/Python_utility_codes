def user_choose():
    """asks the user for factorial or combination calculator"""
    ask = int(input("\n[1] for factorial\n[2] for permutation\n[3] for combination: "))

    if ask == 1:
        num = int(input("\nEnter a number: "))
        print(f"\nOutput: {num}! is",factorial(num))
    elif ask == 2:
        N = int(input("Enter total of numbers in a set: "))
        r = int(input("Enter the number of choosen objects from a set: "))
        print("Output: The number of ways is", permutation(N,r, (factorial)))
    elif ask == 3:
        N = int(input("\nEnter total of numbers in a set: "))
        r = int(input("Enter number of choosing objects from a set: "))
        print(f"\nOutput: The number of combinations is",combination(N,r,(factorial)))
    else:
        print("\n--Unknown Command, Try again!--\n")
        user_choose()

    again = int(input("\nWould you like to\n[1] - Yes\n[2] - No\n>>> "))
    if again == 1:
        user_choose()
    else:
        print("\nGoodbye!")


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#N= Total numbers of distinct items, r=number of items to arrange, and f=factorial method
#order matters
def permutation(N, r, f):
    Permu = f(N) / f(N - r)
    return int(Permu)

#order doesnt metter
def combination(N,r,f):
    Combi = f(N) / (f(N - r) * f(r))
    return int(Combi)

user_choose()