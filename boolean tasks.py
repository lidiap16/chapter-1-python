#lidia pasiecznik 4/10/24
#tasks boolean
# 
# #task
# import random
# number = random.randint(1, 10)
# print(number)
# 
# guess = int(input("enter a number between number between 1 - 10"))
# 
# if guess == number:
#     print("your guess was correct")
#     print("well done")
#     print("play again soon")
# else:
#     print("hard luck")
#     print("incorrect guess")
#     print("play again soon")
#     
# print("goodbye")
# 


#task 5
"""!= is different, play again
soon is on the end of the code in the first code"""

#task 6
import random
n1 = random.randint(0, 12)
n2 = random.randint(0, 12)
print("%d * %d" %(n1,n2))
ans = n1*n2
ans = int(input("enter your answer: "))
if ans == n1*n2:
    print("correct")

else:
    print("incorrect")
    print("the correct answer was %d" %(n1*n2))


