# Micheál Cannon - problem set question 7

# Program that that takes a positive floating point number as input and outputs
# an approximation of its square root.

# Ask user to input number to find the approximate square root of, and assign it to variable "rootof". 
# Found here  https://stackoverflow.com/a/33944290   how to change integer values inputted into floating point numbers
rootof = float(input("Please enter a positive number: "))

# I'm using the Newton Square Root method as described in the lecture in week 8. 
# I've chosen 1.0 as an initial estimate for this method
estimate = 1.0

# Loop that runs until the square of my estimate is within 0.1 of the input
while abs((estimate*estimate) - rootof) > 0.1:

# Newton's method as outlined in the lecture
    estimate -= ((estimate * estimate) - rootof) / (2 * estimate)

# Print the result
print(f"The square root of {rootof} is approx. {estimate}.")