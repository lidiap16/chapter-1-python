#lidia pasiecznik
#decimal to hex

# decimalInput = int(301)
# binaryOutput = " "
# while decimalInput > 0:
#     remainder = decimalInput % 16
#     binaryOutput = str(remainder) + decimalInput
#     decimalInput = decimalInput // 16
# print(decimalOutput)
    
decimalInput = int(input("enter number: ")) # input to convert
binaryOutput = " " # string is created
while decimalInput > 0: #while loop while number is grater that 0
    remainder = decimalInput % 16  #get the remainder from dividing by 2
    binaryOutput = str(remainder) + binaryOutput #gets remainder put it to string; so no math and adds (1 or 0) to the start of the string
    decimalInput = decimalInput // 16 #updates the num by dividing by 2
    if remainder = 10:
        remainder = "A"
    elif remainder = 11:
        remainder = "B"
    elif remainder = 12:
        remainder = "C"
    elif remainder
print(binaryOutput) # prints output

    
    
    
    

