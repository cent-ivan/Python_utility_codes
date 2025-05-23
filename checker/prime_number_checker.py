import time

start = time.perf_counter()
length = 19
for i in range(2,length + 1):
    for j in range(2,i):
        if i % j == 0:
            print(f"{i} = {j} x {i // j}")
            break #break statement to avoid duplicated output
    else:
        print(i,"is a prime number")

end = time.perf_counter()
elapse_time = end - start
print(f"{elapse_time} seconds")
