#lidia pasiecznik 1/10/24
#hw tasks lists

#task 7

userList = []
userName = input("enter your name: ") # prompts user to enter their name
userList.append(userName)
userAge = int(input("what age are you "+userName+"?")) # prompts user to enter their age
userList.append(userAge)
userCountry = input("what is your country of birth?") # prompts user to enter their country of birth
userList.append(userCountry)
userBirth = input("your year of birth:") # prompts user to enter their year of birth
userList.append(userBirth)

print("my database for "+userName+"\n"+str(userList)) #prints out all the information stored in userList

userList.reverse()
print(userList)


#task 8

panList = ["the", "five", "boxing", "wizards", "jump", "quickly"]
print(panList[5],panList[4],panList[:4])

list1 = (panList[:4])
list2 = (panList[4:])
list2.reverse()
print(list2+list1)

#book pg 43 task 3
listrain = []
for i in range(7):
    rain = int(input(f"enter rain every day {i+1}: "))
    listrain.append(rain)
print(listrain)
print(listrain[0]+listrain[1]+listrain[2]+listrain[3]+listrain[4]+listrain[5]+listrain[6], "cm of rain over the week")
print((listrain[0]+listrain[1]+listrain[2]+listrain[3]+listrain[4]+listrain[5]+listrain[6]) / 7)


#task 9

# import random
# fruitFile = open("fruits.txt","r")
# #fruitFile = ["cherry", "melon", "banana", "pineapple", "strawberry"]
# fileContents = fruitFile.read()
# fruitFile.close()
# fruits = fileContents.split()
# print(random.choice(fruits))
# print(random.choice(fruits))
# print(random.choice(fruits))