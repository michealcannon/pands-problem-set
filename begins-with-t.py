# Micheál Cannon - problem set question 2
# A program that outputs whether or not today is a day that begins with the letter T
# Adapted from this post  https://stackoverflow.com/a/9847269


 # import the datetime module

import datetime
# check if today is Tuesday and print confirmation that today begins with a t
if datetime.datetime.today().weekday() == 1:
     print("Yes - today begins with a T")

# check if today is Thursday and print confirmation that today begins with a t
elif datetime.datetime.today().weekday() == 3:
     print("Yes - today begins with a T")

# if today isn't Tuesday or Thursday, print that today doesn't begin with a t
else:
    print("No - today does not begin with a T")