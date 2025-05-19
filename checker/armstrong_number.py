print("This program finds if a number is an Armstrong number or not.".upper())

def is_armstrong():
    number = input("\nEnter a number: ")
    exponent = len(number)
    sum = 0

    for num in number:
        sum += int(num) ** exponent

    if sum == int(number):
        print(f"\nOutput: {number} is an Armstrong number")
    else:
        print(f"\nOutput: {number} is not an Armstrong number")

def ask_user(): #User interaction snippet
    userChoice = int(input(
    """
    \nChoose an action
    [1] - To enter a number
    [2] - Cancel
    [3] - What is the Armstrong number
    >>> """))

    if userChoice == 1:
        is_armstrong()
    elif userChoice == 2:
        print("\nProgram: Thank User")
    elif userChoice == 3:
        print("""\n\tThe Armstrong number definition is the number in any given base, 
        which forms the total of the sae number, when each of its digits is raised 
        to the power of the number of digits in the number. - Jigsawacademy.com, 2021
        
        Examples of Armstrong Number:
        153 = 1^3 + 5^3 + 3^3""")
        ask_user()
    else:
        print("\nProgram: Invalid command")
        ask_user()

ask_user()

