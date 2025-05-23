import time

start = time.perf_counter() #starts the performance timer
#-Code here-------------------------------------------

length = 19
for base in range(2,length + 1):
    for i in range(2,base):
        #checks if the base loop IS DIVISIBLE by that number, divisible meaning can be divided by other number (with 0 remainder)
        if base % i == 0:
            print(f"2. {base} = {i} x {base // i}\n")
            break #stops because it can be divided by other numbers and has no ramainder, break statement to avoid duplicated output
    
    #if the base has a remainder when divided to a number, meaning it has NO DIVISIBLE numbers or CONNOT BE DIVIDED by any whole number
    else:
        print(base,"is a prime number\n")

#----------------------------------------------------
end = time.perf_counter()
elapse_time = end - start
print(f"{elapse_time} seconds")
