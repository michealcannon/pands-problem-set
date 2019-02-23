# Micheál Cannon - question 4

# a program that asks the user to input any positive integer and outputs the
# successive values of the following calculation. At each step calculate the next value
# by taking the current value and, if it is even, divide it by two, but if it is odd, multiply
# it by three and add one. The program ends if the current value is one.

# ask user to enter a positive integer
i = int(input("Please enter a positive integer: "))

# print input 
print(i)

# loop that runs while i does not equal 1
while i != 1:
    
    # divide i by 2 if it is even
    if i % 2 == 0:
        i = i//2

     # multiply i by 3 and add 1 if it is odd   
    else:
        i = (i * 3) + 1

# print value of i
    print(i)
