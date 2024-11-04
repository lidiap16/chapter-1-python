#lidia pasiecznik
#decimal to hex

# decimalInput = int(301)
# binaryOutput = " "
# while decimalInput > 0:
#     remainder = decimalInput % 16
#     binaryOutput = str(remainder) + decimalInput
#     decimalInput = decimalInput // 16
# print(decimalOutput)
    
decimalInput = int(input("enter number")) # to convert
binaryOutput = " " # string is create
while decimalInput > 0: #while loop while number is grater that 0
    remainder = decimalInput % 16  #get the remainder from dividing by 2
    if remainder == 10:
        letter = "A"
    elif remainder == 11:
        letter = "B"
    elif remainder == 12:
        letter = "C"
    elif remainder == 13:
        letter = "D"
    elif remainder == 14:
        letter = "E"
    elif remainder == 15:
        letter = "F"
    else:
        binaryOutput = str(remainder) + binaryOutput
    decimalInput = decimalInput // 16 #updates the num by dividing by 2
print(binaryOutput, letter)

    
    

    
