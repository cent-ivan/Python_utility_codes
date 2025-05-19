#for triangle

#standing traingle
add = 1
for x in range(5,-1,-1):
    for y in range(x,-1,-1):
        print(end=" ")
        

    print("* " * add)
    add += 1

#reverse triangle 
add2 = 5
for i in range(1,6 + 1):
    for j in range(i + 1):
        print("",end=" ")
    
    print("* " * add2)
    add2 -= 1

#Inverse triangle
n = int(input("Enter Row: "))
triangle = ""

multi = n
space = 1

print()
for row in range(n, 0, -1):
    for column1 in range(row):
        triangle += "*"

    triangle += (" " * space)
    triangle += ("*" * multi)
    
    multi -= 1
    space += 2
    triangle += "\n"
triangle += ("*" * ((n * 2) + 1))
    
print(triangle)