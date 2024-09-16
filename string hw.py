#lidia pasiecznik 16/09/24
#hw tasks, strings

#task 4
#1
word1 = "Leaving"
word2 = "certificate"
word3 = "computer"
word4 = "science"
subjectName = word1 + word2 + word3 + word4
print(subjectName)

#2
pangram = "the quick brown fox jumps over the lazy dog!"
print(pangram[:3] + pangram[16:]) # this should have a 4 instead of a 3 to add a space between the words tha and fox

#3
noun = input("enter a singular noun:")
print("the plural of "+noun+" is "+noun+"s")