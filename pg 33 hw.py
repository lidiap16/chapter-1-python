#lidia pasiecznik
#13/10/24 hw qs pg 33

#task 1
# start = 1000
# end = 1500
# total = 0
# current = start
# while current <= end:
#     total += current
#     current += 1
#     
# print(total)
# 
# #task 2
# 
# count = 0
# total = 0
# while count < 6:
#     number = float(input("enter a number:"))
#     total += number
#     count += 1
# average = total / 6
# print(average)

#task 3
# password = False
# while password == False:
#     name = str(input("enter name: "))
#     if name == "Maureen":
#         print("welcome Maureen")
#         break;
#     else:
#         print("wrong")
# while password == False:
#     passnum = input("enter password")
#     if passnum == "1234":
#         print("welcome")
#         break;
#     else:
#         print("access denied")

#task 4
num = 1
eventotal = 0
oddtotal = 0
limit = int(input("enter num greater that 0: "))
while num <= limit:
    if num % 2 == 0:
        eventotal += num
    else:
        oddtotal += num
    num += 1
print(eventotal)
print(oddtotal)



# limit = int(input("enetr num"))
# for num in range(1, limit + 1):
#     if num % 2 == 0:
#         eventotal += num
#     else:
#         oddtotal += num
# print(eventotal)
# print(oddtotal)
#            