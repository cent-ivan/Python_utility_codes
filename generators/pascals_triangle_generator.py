print("Pascal's Triangle Generator")
number = int(input("\nEnter Row: "))

def factorial(n):   #Factorial (Recursion)
    if n == 0:          #Base Case
        return 1
    else:
        return n * factorial(n - 1)

#Formula for generating the numbers in the Pascal's triangle
Combination = lambda n,k,factorial: factorial(n) // (factorial(k) * (factorial(n-k)))

#Pascal's triangle formation-------------------------------
i = number 
for row in range(number + 1):
    for x in range(i,0,-1):     #Loop for the negative spaces
        print(end="    ")  
    for num in range(row + 1):  #loop for the numbers to be put on the Pascal Triangle
        print(Combination(row,num,factorial),end="       ")
        
    print()
    i -= 1  
#----------------------------------------------------------