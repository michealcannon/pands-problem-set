# Micheál Cannon 22/3/2019 
# Problem set question 8

# program that outputs today’s date and time in the format “Monday,January 10th 2019 at 1:15pm”. 

# I adapted some of the code from this stack overflow post  https://stackoverflow.com/a/48947064
# I found out how the strftime method here https://www.programiz.com/python-programming/datetime/strftime

from datetime import datetime

# returns current month as a string and assigns it to variable "month"
month = datetime.now().strftime('%B ')

# assigns string of current day to "day"

day = datetime.now().strftime('%A')

# today's date as ordinal
# adapted from this post https://stackoverflow.com/a/18670679
date = datetime.now().strftime('%d')

if date ==" 1" or date ==" 21" or date ==" 31":
     suffix = "st"
elif date == "2" or date ==  "22":
     suffix = "nd"
elif date == "3" or date == "23":
     suffix = "rd"
else:
   suffix = "th"

dateord = date + suffix

# returns current year

year = datetime.now().strftime(' %Y')

# current time in 12 hour format

time = datetime.now().strftime('%H:%M:%p')

print(day + ', ' + month + dateord + year + ' at ' + time)
