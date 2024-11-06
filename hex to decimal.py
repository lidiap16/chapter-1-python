#lidia pasiecznik
#hex to decimal

base = int(input("enter base : "))
binary_input = input("enter hex code: ")
decimal_output = int(binary_input, base) 
print(decimal_output)

if binary_input == "F":
    decimalOutput = 15*(base**binary_input)

if binary_input == "E":
    decimalOutput = 14*(base**binary_input)

if binary_input == "D":
    decimalOutput = 13*(base**binary_input)

if binary_input == "C":
    decimalOutput = 12*(base**binary_input)

if binary_input == "B":
    decimalOutput = 11*(base**binary_input)

if binary_input == "A":
    decimalOutput = 10*(base**binary_input)

#lidia pasiecznik
#decimal to BINARY
decimalInput = decimal_output
#decimalInput = int(input("enter number: ")) # input to convert
binaryOutput = " " # string is created
while decimalInput > 0: #while loop while number is grater that 0
    remainder = decimalInput % 2  #get the remainder from dividing by 2
    binaryOutput = str(remainder) + binaryOutput #gets remainder put it to string; so no math and adds (1 or 0) to the start of the string
    decimalInput = decimalInput // 2 #updates the num by dividing by 2
print(binaryOutput) # prints output

#
# binary_input = input("enter binary code: ")
# decimal_output = int(binary_input, 2) # converts the binary string to a decimal intiger. the 2 specifies that the input is in base 2
# print(decimal_output)


# val = input("Please enter hex value to be converted: ")
# base = 16 # Used in calculation of base number
# vals = [] # Will hold the value to be converted, once checked for decimal equivalents and all converted to integers
# 
# # Check value to be converted and update values A, B, C, D, E, F to decimal equivalents
# # Add values to a list
# counter = 0
# while counter < len(val):
#     if val[counter] == "A":
#         vals.append(10)
#     elif val[counter] == "B":
#         vals.append(11)
#     elif val[counter] == "C":
#         vals.append(12)
#     elif val[counter] == "D":
#         vals.append(13)
#     elif val[counter] == "E":
#         vals.append(14)
#     elif val[counter] == "F":
#         vals.append(15)
#     else :
#         vals.append(int(val[counter]))
#     counter += 1
# 
# # Reverse the list so index corresponds to powers of base number
# vals.reverse()
# 
# # Find the decimal value
# count = 0
# total = 0
# while count < len(vals):
#     total += (vals[count]*(base**count))
#     count +=1
# 
# print("Number being converted:", val)
# print()
# print("Modified value with hex written as decimal, and number reversed:", vals)
# print()
# print("Converted value:", total)