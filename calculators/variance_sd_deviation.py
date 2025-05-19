import math

nLen = int(input("Enter Length: "))


class VarianceAndStDeviationCalculator:
    def __init__(self) -> None:
        self.nList = [] #values
        self.mean = 0

    def add_to_list(self, nLen) -> None:
        for i in range(nLen):
            var = float(input(f"{i + 1}. "))
            self.nList.append(var)

    def compute_variance(self, arr,mean, length) -> float:
        temp_list = []
        for x in arr:
            dif = x - mean #decrease each item by the mean
            sqr = round(dif ** 2, 2) #square the difference and add to a temp list
            temp_list.append(sqr)

        total = sum(temp_list) #adds all
        return round(total / length, 2)
    
    def compute_mean(self, nList:list, nLen) -> float:
        return sum(nList) / nLen

calculator = VarianceAndStDeviationCalculator()
calculator.add_to_list(nLen) #calls to add list

mean = calculator.compute_mean(calculator.nList, nLen)
variance = calculator.compute_variance(calculator.nList, mean, nLen) #Variance tells you how "off" the data is on average (squared). Think of variance like squaring how far your darts are from the center — it's useful for calculation.
standard_deviation = math.sqrt(variance) #Standard deviation brings it back to original units (by square rooting variance), making it easier to interpret. Think of standard deviation like the average distance your darts are from the bullseye — it tells you in real units how consistent your throws are.


print(f"The mean is {mean}\nThe Variance is {variance} \nThe Standard Deviation is {standard_deviation}")