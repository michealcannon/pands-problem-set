# Micheál Cannon - problem set question 6

# A program that takes a user input string and outputs every second word.


# Ask for user to input a sentence. 
# assign a list of words in the string inputted to a variable s
# I found the method for doing this in the python documentation here https://docs.python.org/3/library/stdtypes.html#string-methods
s = str.rsplit(input("please enter a sentence: "))

# assign a new empty list to a variable l
l = []

# a loop that runs through the even numbered items in list s...
n = 0
while n < len(s) / 2:

# and adds these items to the list l. I found the append method in the python tutorial 3.1.3
    l.append(s[2 * n])
    n = n + 1

# print the items in list l as a string
print (" ".join(l))


