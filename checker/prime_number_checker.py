length = int(input("Enter a number: "))
for i in range(2,length + 1):
    for j in range(2,i):
        if i % j == 0:
            print(f"{i} = {j} x {i // j}")
            break #break statement to avoid duplicated output
    else:
        print(i,"is a prime number")
