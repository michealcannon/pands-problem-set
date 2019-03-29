# Micheál Cannon - question 6
#  a program that asks the user to input a positive integer and tells the user whether or not the number is a prime. 

# ask for user to input a positive integer; convert to int value and assign to variable i
i = int(input("Please enter a positive integer: "))

# if user inputs 1, print "This is not a prime"
if i == 1:
        print("This is not a prime")
else:
        
# If user doesnt input 1, loop that checks if 2,3,4,...,i-1 can divide into i with no remainder
        for n in range (2,i):
                if i % n == 0:

# prints "this is not a prime" and breaks the loop as soon as a factor of i is found
                        print("This is not a prime")
                        break

# prints "this is a prime" if the loop ends without a break (no factor is found)
        else:
                print("This is a prime")
