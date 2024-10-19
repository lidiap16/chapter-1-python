#lidia pasiecznik
#test cases

#Date:
# Description: Working with test cases

# radius = float(input("Enter radius: ")) 
# if radius > 0:
#     volume = (4/3*3.14*radius**3)
#     print("The volume is: ", volume)
#     print(round(volume,2))
# else:
#     radius == str
#     print("invalid character")
while True:   #start of loop
    try:  #tryes the code
        radius = float(input("enter a positive radius: ")) #asks the user to input the radius, attempting to convert the input to a float
        if radius > 0: # checks for positive number
            break #exits the loop
        else:
            print("please enter a positive number") #prompt for positive value
    except ValueError: 			#handle the case where the input is not a number
        print("invalid input. please enter a positive number")
volume = (4/3*3.14*radius**3) #calculates the volume
print("the volume is:", round(volume, 2)) #prints rounded volume
"""
test run 1
***************************************************************
#ID   #Description       #test data #Expected  #Actual  #Passed
#     #                  #          #RESULT    #result  # y/n
***************************************************************
"""
#6  #test a regular value #6        #904.32    #904.3199 #no
#**************************************************************
#2  #test a large number  #4096     #2.877055  #287705542601.38666 #yes    
                                    #10^11
#**************************************************************
#3  #test a negative no   #-2       #imput     #-33.4933  #no   
                                    #invalid
#**************************************************************
#4  #test dcimal          #2.7      #82.40616   #82.40616000000002 #no
#**************************************************************
#5  #test 0               #0        #0         # 0.0  #yes   
#**************************************************************
#6  #test input string    #hello    #errror    #error #yes

"""
***************************************************************
#ID   #Description       #test data #Expected  #Actual  #Passed
#     #                  #          #RESULT    #result  # y/n
***************************************************************
"""
#6  #test a regular value #6        #904.32    #904.32 #yes
#**************************************************************
#2  #test a large number  #4096     #2.877055  #287705542601.39 #yes  
                                    #10^11
#**************************************************************
#3  #test a negative no   #-2       #prompts      #prompts #yes
                                    #again         again 
#**************************************************************
#4  #test dcimal          #2.7      #82.40616     #82.41  #no
#**************************************************************
#5  #test 0               #0        #prompts again #prompts again #yes
#**************************************************************
#6  #test input string    #hello    #prompts again #prompts again #yes