# Micheál Cannon Problem Set Question 1
# A program that asks the user to input a positive integer and outputs the sum of all numbers between 1 and that number

# Convert user input to int value and assign to variable i
i = int(input("Please enter a positive integer: "))

# Set variable n to be 1 less than number input by user
n = i - 1

# Loop that adds n to user input, then decrements n by 1. Loop ends when n is 0.
while n > 0:
    i = i + n
    n = n - 1

# Print sum of all numbers between 1 and user input
print(i)