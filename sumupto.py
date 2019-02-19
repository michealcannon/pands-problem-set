#  Problem Set Question 1
# A program that asks the user to input a postive integer and outputs the sum of all numbers between 1 and that number

i = int(input("Please enter a positive integer: "))
n = i - 1
while n > 0:
    i = i + n
    n = n - 1

print(i)