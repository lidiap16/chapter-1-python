#lidia pasiecznik 6/10/24
#tasks book hw


#task1
num1 = int(input("enter number"))
num2 = int(input("enter number"))

if num2 % num1 == 0: # use % => modulus  remainder ?
    print("divides")
else:
    print("doesnt divide")
    
    
#task2
        
age = int(input("enter age"))
if age >= 17:
    print("you are eligible")
else:
    print("your are not old enough")

""" 
                                    / equal -> print " you are eligible "
                                   /
enter age-> if age grater or equal<
                                   \
                                    \ else -> print " you are not old enough "
"""
                                
#lidia pasiecznik 8/10/24
#book tasks pg 30

#task 3

item = int(input("enter cost of item: "))	# input cost 
if item > 10000:
    print("go to tender") 	 #if item costs more than 10000 it prints go to tender
elif item >= 500 and item <= 10000:		
    print("get quotes from threedifferent suppliers") 		# else if the item costs more than 500 and under 10000 it prints: get quotes....
else:
    print("order item") #else it prints order item
    
#task 4
    
print(" A. dundrum shopping centre") #menue
print(" B. tallaght")
print(" C. broombridge")
    
trip = input("where u wanna go") # asks to imput destination

if trip == "A":
    print("you have won a ticket to dundrum shopping centre") # if A it prints the text
elif trip == "B":
    print("you have won a ticket to tallaght") #if B it prints the text
elif trip == "C":
    print("you have won a ticket to broombridge") # if C it prints the text
else:
    print("invalid entry") # else it prints invalid entry

#task 5
percentage = int(input("enter percentage")) # asks for input of a percentage

if 90<= percentage <=100:	# if its over 90 and under 100 it prints H1
    print("H1")
elif 80<= percentage <= 89: # ELSE IF the percentage is over 80 and under 89 it prints H2, 
    print("H2")				#it does this with the rest of the elifs juist with dif percentages
elif 70<= percentage <= 79:
    print("H3")
elif 60<= percentage <= 69:
    print("H4")
elif 50<= percentage <= 59:
    print("H5")
elif 40<= percentage <= 49:
    print("H6")
elif 30<= percentage <= 39:
    print("H7")
elif 0<= percentage <= 29:
    print("H8")
else:
    print("invalid percentage") # if non of the above ifs are made itll print invalid percentage





