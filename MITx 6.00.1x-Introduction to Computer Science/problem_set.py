## Problem 1
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5


# s = input("Input: ")
# numVowels = 0
# while True:
#     for i in s:
#         if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#             numVowels += 1
#         else:
#             continue
#     break
# print("Number of vowels: ", numVowels)

## Problem 2

# s = 'azcbobobegghakl'
# wanted = 'bob'
# numofBob = 0
# n = 0
#
# for i in range(len(s)):
#     a = s[n:n + 3]
#     n += 1
#     if a == wanted:
#         numofBob += 1
# print(numofBob)

## Problem 3
# longest string, in any given time I want to find sequence in alphabet, same for alphabet,
s = 'azcbobobegghakl'
# I want to keep track of the longest word
newS = ""
# Another string to keep track of
tempS = ""
# iterate over word
for i in range(1, len(s)):
    # check if neighbor bigger than me
    if s[i] >= s[i-1]:
        # Then you are on the right track, and you want to add this into newS variable.
        newS += s[i]
        # Is your current substring longer than any previous one?
        if len(newS) > len(tempS):
            tempS = newS
    else:
        newS = s[i]
print(tempS)




