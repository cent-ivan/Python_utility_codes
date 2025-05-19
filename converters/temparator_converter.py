def ask():
    choice = int(input("[1]- Convertert Fahrenheit to Celsius\n[2]- Convert Celsius to Fahrenheit\n: "))
    if choice == 1:     #If user choose 1, it calls the fahrenheit to celsius function
        print(f"{fah_to_cel()} Celsius")
    elif choice == 2:   #If user choose 2, it calls the celsius to fahrenheit function
        print(f"{cel_to_fah()} Fahrenheit")
    else:
        print("\n[!] Unknown Command")  #prints the string when user enters neither 1 and 2

def fah_to_cel():  #the function calculates the fahrenheit to celsius
    print()
    Fahrenheit = int(input("Enter Fahrenheit: "))
    Celsius = (Fahrenheit - 32) * 5/9   #formula for the convertion of fahrenheit to celsius
    return Celsius

def cel_to_fah(): #the function calculates the celsius to fahreheit
    print()
    Celsius = int(input("Enter Celsius: "))
    Fahrenheit = 9/5 * Celsius + 32     #formula for the convertion of celsius to fahrenheit
    return Fahrenheit

ask()