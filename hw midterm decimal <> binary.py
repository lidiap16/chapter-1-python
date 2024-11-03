#lidia pasiecznik
#decimal to BINARY
decimalInput = int(input("enter number: ")) # input to convert
binaryOutput = " " # string is created
while decimalInput > 0: #while loop while number is grater that 0
    remainder = decimalInput % 2  #get the remainder from dividing by 2
    binaryOutput = str(remainder) + binaryOutput #gets remainder put it to string; so no math and adds (1 or 0) to the start of the string
    decimalInput = decimalInput // 2 #updates the num by dividing by 2
print(binaryOutput) # prints output

#
binary_input = input("enter binary code: ")
decimal_output = int(binary_input, 2) # converts the binary string to a decimal intiger. the 2 specifies that the input is in base 2
print(decimal_output)
