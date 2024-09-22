#lidia pasiecznik 22/09/24
#hw tasks pg 25

#task 4

seconds = int(input("enter number in second:"))
minutes = round(seconds / 60)
print("minutes = ", minutes)

#task 5

char = input("enter a character: ")
print(ord(char))
char = input("enter a character: ")
print(ord(char))
char = input("enter a character: ")
print(ord(char))
char = input("enter a character: ")
print(ord(char))
char = input("enter a character: ")
print(ord(char))

#task6

unitsUsed = int(input("enter the number of units of electricity used: "))
ratePerUnit = 0.19
standingCharge = 26.20
totalCost = (unitsUsed * ratePerUnit) + standingCharge
print(totalCost)

#task7

fish = 4.50
chips = 2.80
vat = 0.09
fishOrder = int(input("enter the num of portions of fish: "))
chipsOrder = int(input("enter the num of portions of chips: "))
totalAmount = (fishOrder * fish) + (chipsOrder * chips)
vatAmount = totalAmount * vat
print("fish order =", fishOrder, "chips order =", chipsOrder)
print("total amount due:",totalAmount)
print("reminder: (9%) vat amount:", vatAmount)
afterVat = round(totalAmount + vatAmount)
print("price after vat added:", afterVat)

#task 8
word = input("enter a 5 letter word:")
key = int(input("key (0,25):"))
letter1 = (word[:1])
ascii1=ord(letter1)
encryptedLetter1 = chr(ascii1 + key)
print(encryptedLetter1)
letter2 = (word[1:2])
ascii2=ord(letter2)
encryptedLetter2 = chr(ascii2 + key)
print(encryptedLetter2)
letter3 = (word[2:3])
ascii1=ord(letter3)
encryptedLetter3 = chr(ascii1 + key)
print(encryptedLetter3)
letter4 = (word[3:4])
ascii1=ord(letter4)
encryptedLetter4 = chr(ascii1 + key)
print(encryptedLetter4)
letter5 = (word[4:5])
ascii1=ord(letter5)
encryptedLetter5 = chr(ascii1 + key)
print(encryptedLetter5)
print(encryptedLetter1 + encryptedLetter2 + encryptedLetter3 + encryptedLetter4 + encryptedLetter5)
