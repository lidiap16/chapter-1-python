#lidia pasiecznik 7/10/24
#onenote tasks

#1
name = input("enter name: ") #ask for name 
if len(name) < 7:	#if name shorter than  7 letters
    print("hello", name, "your name is short") #prints short name
if len(name) >= 7 and len(name) <= 10:	#if name between 7 and 10 letters long
    print("hello", name, "your name is long") #prints long name 
if len(name) > 10:
    print("hello", name, "your name is very long ") #else print very long name
    
#task2

print(" 1. music ")	# MAIN menue
print(" 2. history ")
print(" 3. design and technology")
print(" 4. exit ")
choice = input("enter choice: ")
if choice == "1":					#choices if statements to print certain answers
    print("you chose music")
if choice == "2":
    print("you chose history")
if choice == "3":
    print("design and technology")
if choice == "4":
    print("goodbye")
    
#task3
    
import random # imports file random

dice1 = random.randint(1,6) # die numbers are chosen at random
dice2 = random.randint(1,6)
print(dice1)
print(dice2)
sumNum = (dice1 + dice2) # adds the random numbers
if dice1 == dice2:
    double = sum(int(dice1 + dice2 * 2))	 # if the die numbers are the sameit prints double the sum
    print("you threw a double")
else:
    print(int(sumNum)) #else sum of the dies

#task4
discount = 0
value = float(input("enter cost of item:"))
if value >= 200:
     discount = value * 0.10
elif 100 <= value < 200:
    discount = value * 0.05

amount = value - discount
print(value)
print(discount)
print(amount)
     
     
#task 5
#order a, d, c, b
     
     
     