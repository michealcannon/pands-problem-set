# Micheál Cannon 26/3/2019 Problem 9
# Program that reads in a text ﬁle and outputs every second line.
# The program takes the ﬁlename from an argument on the command line.

# Import the sys module in order to access sys.argv
import sys

# Open the file in the command line argument in order to read it. Assign file to variable "f"
with open(sys.argv[1], "r") as f:


   # I adapted the code in this example https://stackoverflow.com/questions/2081836/reading-specific-lines-only to print evry second line

   # loop that enumerates each line in the text file and..
    for i, line in enumerate(f):

        # ... prints every even numbered line
        if i % 2 == 0:
            print(line)
    


