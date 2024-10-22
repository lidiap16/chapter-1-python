#lidia pasiecznik
#tasks pg 46
#task 2

# payType = input("do you want to pay using cash,card or coupon?")
# if payType == "cash":
#     print("PLEASE insert cash.")
# elif payType =="card":
#     print("insert card into the machine.")
# else:
#     print("coupons are only accepted at customer service.")
    
"""        
*********************************************************************************************
id    #description    #test data   #expecter value   #actual result  #passed (y/n)
*********************************************************************************************
#1    #enter cash     #cash        #please enter cash #please enter cash  #yes
*********************************************************************************************
#2    #enter card     #card        #insert card...... #insert card...   #yes
*********************************************************************************************
#3    #enter coupon   #coupon      #coupons are...    #coupons are...   #yes
*********************************************************************************************
#4    #enter string    #hello       #invalid try again  #coupons are...   #no
*********************************************************************************************
#5    #enter number   #15          #invalid try again  #coupons are...   #no
*********************************************************************************************

"""

#task 3

counter = 0
while counter < 7:
    print(counter)
    counter += 1
print("im glad that the loop is finished")

"""
*********************************************************************************************
id    #description   #expecter value   #actual result  #passed (y/n)
*********************************************************************************************
#1    #does it satart at 0 # 0 printed first #0 printed first #yes
*********************************************************************************************
#2    #does it get to < 7  #0,1,2,3,4,5,6  #0,1,2,3,4,5,6 #yes
*********************************************************************************************
#3    #exits at 7   #loopends after 6 and prints text#loopends after 6 and prints text # yes
*********************************************************************************************
#4    #boundry test        #runs while counter < 7     #loop runs while counter        #yes
                       exits correctly at counter = 7  < 7 and exits after counter = 7
********************************************************************************************
"""


