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

item = int(input("enter cost of item: "))
if item > 10000:
    print("go to tender")
elif item >= 500 and item <= 10000:
    print("get quotes from threedifferent suppliers")
else:
    print("order item")
    
#task 4
    
print(" A. dundrum shopping centre")
print(" B. tallaght")
print(" C. broombridge")
    
trip = input("where u wanna go")

if trip == "A":
    print("you have won a ticket to dundrum shopping centre")
elif trip == "B":
    print("you have won a ticket to tallaght")
elif trip == "C":
    print("you have won a ticket to broombridge")
else:
    print("invalid entry")

#task 5
percentage = int(input("enter percentage"))

if 90<= percentage <=100:
    print("H1")
elif 80<= percentage <= 89:
    print("H2")
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
    print("invalid percentage")





