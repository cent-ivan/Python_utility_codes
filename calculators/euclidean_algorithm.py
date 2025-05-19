#Euclidean Algorithm by Vincent Ivan Palomata
"""a method for efficiently finding the greatest common divisor (GCD) of two integers."""
A = int(input("Enter Number: "))
B = int(input("Enter Number: "))
result = []
GCD = []

def algo(A, B): 
    table_row = []

    Q = A // B
    table_row.append(Q)
    table_row.append(A)
    table_row.append(B)
    R = A % B
    table_row.append(R)

    result.append(table_row)

    if R == 0:
        GCD.append(table_row[2])
        pass
    else:
        A = B
        B = R
        algo(A, B)

algo(A, B)



print("Q |  A |  B | R") #Q= qoutient, A= first number, B= second number, R= remainder
for i in result:
    print(i)

LCD = (A * B) // GCD[0]
print(f"\nThe Greatest Common Divisor is {GCD[0]}")
print(f"The Least Common Multiple is {LCD}")