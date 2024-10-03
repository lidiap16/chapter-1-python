#lidia pasiecznik 3/10/24
#hw tasks, boolean

import random
number = random.randint(1, 10)
print(number)
guess = int(input("enter no. 1-10 : "))
if guess == number:
    print("correct")
    print("well done")
else:
    print("incorrect")
print("goodbye")