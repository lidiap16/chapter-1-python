#lidia pasiecznik
#13/10/24 hw qs pg 33

#task 1 # adds numbers between 1000 to 1500
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
# #task 2 # takes 6 nums and divides by 6 fo average
# 
# count = 0
# total = 0
# while count < 6:
#     number = float(input("enter a number:"))
#     total += number
#     count += 1
# average = total / 6
# print(average)
# print(round(average))
# 
# #task 3
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
# num = 1
# eventotal = 0
# oddtotal = 0
# limit = int(input("enter num greater that 0: "))
# while num <= limit:
#     if num % 2 == 0: # modulous if = to zero even number + 1 
#         eventotal += num
#     else:
#         oddtotal += num #else add total to num
#     num += 1
# print(eventotal)
# print(oddtotal)
# 
# #task 5
# average = 0
# number = True
# number2 = 0
# while number:
#     NumINPUT = int(input("enter num"))
#     if NumINPUT < 1:
#         number = False
#         break
#     average += NumINPUT
#     number2 += 1
# average = average/number2
# print(average)

#task 6
# 
# sentence = input("enter words")
# wordcount = sentence.count(" ")
# print(wordcount+1)

#task7
print("**************************")
print("| 1. curtains            |")
print("| 2. cushion covers      |")
print("| 3. quilts              |")
print("| 4. exit                |")
print("**************************")
 
choice = input("enter choice: ")
if choice == "1":
    print("you chose, curtains, 10$ for 1m^2")
    size = int(input("enter size: "))
    cost = size * 10
    print("cost of curtain is", cost, "$")
elif choice == "2":
    print("you chose, cushon covers")
    color = input("choose cloror, red, blue, green, yellow, flowery: ")
    if color == "red":
         print("cushon cover costs 8$")
    elif color == "blue":
         print("cushon cover costs 8$")
    elif color == "green":
         print("cushon cover costs 8$")
    elif color == "yellow":
         print("cushon cover costs 8$")
    elif color == "flowery":
         print("cushon cover costs 10$")
    else:
        print("no such color")
elif choice == "3":
    print("you chose option, quilts")
    colour = input("enter color: ")
    print("you chose a", colour, "quilt, costs 10%")
elif choice == "4":
    print("you sure you want to leave")
        
        