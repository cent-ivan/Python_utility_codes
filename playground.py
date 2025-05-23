
import time

start = time.perf_counter()

def is_prime(number:int): 
    count = 0
    for base in range(1, number + 1):
        if number % base == 0:
            count += 1
    
    if count > 2:
        print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")
        # print(f"{number} / {base} == {number / base}")


for i in range(2, 19):
    is_prime(i)

end = time.perf_counter()
elapse_time = end - start
print(f"{elapse_time} seconds")