#lidia pasiecznk 29/09/24
#hw pg 42

#task 1

numbers = []
for i in range(5):
    nums = int(input(f"enter numbers {i+1}: "))
    numbers.append(nums)
print(numbers)

addNum = [nums + 1 for nums in numbers]
print(addNum)


#task2
hours = [12, 7, 9, 9, 6, 8, 2]
totalmilk = 0.5 * sum(hours)
print(totalmilk)

costmilk = 1.35
totalcost = costmilk * totalmilk
print(int(totalcost))