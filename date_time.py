# Micheál Cannon 22/3/2019 
# Problem set question 8

# program that outputs today’s date and time in the format “Monday,January 10th 2019 at 1:15pm”. 

# I adapted some of the code from this stack overflow post  https://stackoverflow.com/a/48947064
# I found out how the strftime method works here https://www.programiz.com/python-programming/datetime/strftime

from datetime import datetime

# returns current month as a string and assigns it to variable "month"
month = datetime.now().strftime('%B ')

# assigns string of current day to variable "day"

day = datetime.now().strftime('%A')

# today's date as an ordinal number.Adapted from this post https://stackoverflow.com/a/18670679

# returns current date as a string
date = datetime.now().strftime('%d')

# Create a string variable called suffix and set it to "st" if today's date is 1, 21 or 31,...
if date ==" 1" or date ==" 21" or date ==" 31":
     suffix = "st"
elif date == "2" or date ==  "22":  # to "nd" if today's date is 2 or 22
     suffix = "nd"
elif date == "3" or date == "23": # to "rd" if today's date is 3 or 23
     suffix = "rd"
else:
   suffix = "th" # to "th" otherwise

# Join suffix to the end of the number for today's date and assign it to variable "dateord" - today's date as an ordinal number
dateord = date + suffix 

# returns current year as a string and assigns it to variable "year"

year = datetime.now().strftime(' %Y')

# current time in 12 hour format. I found it here.. https://discuss.codecademy.com/t/how-to-convert-to-12-hour-clock/3920/3

time = datetime.now().strftime('%I:%M:%p')

# strings referred to by variables "day", "month", "dateord", "year" and "time" concatenated to show time in required format
print(day + ', ' + month + dateord + year + ' at ' + time)
