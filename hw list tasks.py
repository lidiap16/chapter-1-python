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


#task 9

import random
fruitFile = open("fruits.txt","r")
#fruitFile = ["cherry", "melon", "banana", "pineapple", "strawberry"]
fileContents = fruitFile.read()
fruitFile.close()
fruits = fileContents.split()
print(random.choice(fruits))
print(random.choice(fruits))
print(random.choice(fruits))