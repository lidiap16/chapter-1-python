#lidia pasiecznik
#13/10/24 hw qs pg 33

#task 1
start = 1000
end = 1500
total = 0
current = start
while current <= end:
    total += current
    current += 1
    
print(total)

#task 2

count = 0
total = 0
while count < 6:
    number = float(input("enter a number:"))
    total += number
    count += 1
average = total / 6
print(average)