
import time

start = time.perf_counter() #starts the performance timer
#-Code here-------------------------------------------
#Accepts keyword arguments, then you can use **.
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        
params = {
    "name" : "Alice",
    "age" : 30,
    "country" : "USA"
}

my_function(**params)

#----------------------------------------------------
end = time.perf_counter()
elapse_time = end - start
print(f"{elapse_time} seconds")