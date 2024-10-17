#lidia pasiecznik
#hw pg 37

# #task 1
# num = 1
# for i in range(1,11):
#     print(num)
#     num+= 1
# 
# num = 1
# 
# while num<= 10:
#     print(num)
#     num+=1
#     
#     
# #task 2
# num = int(input("enter number"))
# num1 = 1
# 
# while num1 <= num:
#     
#     num1+=1
#     if num1 % 2:
#         print(num1)
# 
# #task3
# sentence = input("enter sentence: ")
# vowels = ['a', 'e', 'i', 'o', 'u']
# vowelList = [char for char in sentence.lower() if char in vowels] # char = character
# print(len(vowelList))  # length

#task 4

sentence = input("enter sentence: ")
sentenceList = list(sentence)
reverseList = []
for char in sentenceList:
    reverseList.insert(0, char) #insert each character at the beginning of the new list
    
reverseSentence =''.join(reverseList) #join the reversed list back into a string
print(reverseSentence)