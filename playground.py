
import time

start = time.perf_counter() #starts the performance timer
#-Code here-------------------------------------------

def is_prime(number:int): 
    count = 0
    for base in range(1, number + 1):
        if number % base == 0:
            count += 1
    
    if count > 2:
        pass
    else:
        print(f"{number} is a prime number")
        # print(f"{number} / {base} == {number / base}")

number = 110
for i in range(2, number  + 1):
    is_prime(i)

#----------------------------------------------------
end = time.perf_counter()
elapse_time = end - start
print(f"{elapse_time} seconds")