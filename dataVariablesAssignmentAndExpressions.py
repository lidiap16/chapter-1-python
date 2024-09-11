"""lidia pasiecznik
assignment tasks"""

#task 1

personName = "Alex"
favouriteColour = "red"
print("hi", personName, "- your favourite colour is", favouriteColour)
print("Goodbye", personName)
#it'll say Alex red

#next it'll say Charlie green there will be no alex or red in the variable section

personName = "Charlie"
favouriteColour = "green"
print("hi", personName, "- your favourite colour is", favouriteColour)
print("Goodbye", personName)

#task 2
personName = input("enter your name: ")
favouriteColour = input("enter your favourite colour: ")
print("hi", personName, "- you favourite colour is", favouriteColour)
print("Goodbye", personName)

#task 3
"""different types of variables cant be a word reserved by python e.g print """

#task 4 

#i think it adds 0 +1 and then prints the text +the value of goals
goals = 0 
goals = goals + 1
print("the value of goals is", goals)

#the computer does the first maths 1+2 and then assaigns a value to value1 and value2 and then prints them
answer = 1+2
print(answer)
value1 = answer+3
value2 = 1+2+3
print(value1, value2)

#the program assignes a to temp and a = b and b = temp 
a = 10
b = 5
temp = a
a= b
b = temp

#it assignes valuse for accountBalance and withdrawaelAmount and subtracts it
accountBalance = 1000
withdrawalAmount = 600
accountBalance = accountBalance - withdrawalAmount

#assignes values to days hrs and mins and then multiplys them and print it
days = 2
hrs = 24
mins = 60
total = days*hrs*mins
print(total)


#task5
year = int(input("enter the current year: "))
age = int(input("what age will you be at the end of this year : "))
print("you were born in", year-age)

#task6
#program to convert from centigrade to fahrenheit
centigrade = float(input("enter the centigrade value: "))
fahrenheit = 9/5 * centigrade + 32
print(centigrade, "degrees C equals", fahrenheit, "degrees F")
# all the values are correct
"""
0/32.0/32
32/89.6/89.6
1000/1832/1832
-10/14/14
-40/-40/-40
-1000/1768/-1768"""
"""it helps to visualise the answeres
 syntax error
"""

#task7

principal = input("enter principal: ")
principal = float(principal)

rate = input("enter rate: ")
rate = float(rate)
 
time = input("enter time in years: ")
time = float(time)
 
amount = principal * rate * time
print("the interest amount is", amount)#

"""
1 rate, principal and time
multiplying
amount after interest rate over x years

2 it would brake, no float
"""

#task8
print(pow(10, abs(-2)))
#abs turns -2 into 2 ?

#