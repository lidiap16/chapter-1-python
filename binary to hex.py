#lidia pasiecznik
#binary to hex
binary_input = input("enter binary code: ")
decimal_Output = int(binary_input, 2) # converts the binary string to a decimal intiger. the 2 specifies that the input is in base 2
print(decimal_Output)

binaryOutput = " "
Output = ""# string is create
base = int(input("enter base: "))
decimalInput = decimal_Output
while decimalInput > 0: #while loop while number is grater that 0
    remainder = decimalInput % base  #get the remainder from dividing by 2
    if remainder == 10:
        binaryOutput = "A" + binaryOutput
    elif remainder == 11:
        binaryOutput = "B" + binaryOutput
    elif remainder == 12:
        binaryOutput = "C" + binaryOutput
    elif remainder == 13:
        binaryOutput = "D" + binaryOutput
    elif remainder == 14:
        binaryOutput = "E" + binaryOutput
    elif remainder == 15:
        binaryOutput = "F" + binaryOutput    
    else:
        binaryOutput = str(remainder) + binaryOutput
    decimalInput = decimalInput // base #updates the num by dividing by 2
print(binaryOutput)


