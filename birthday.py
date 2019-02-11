"""
birthday.py
Author: Esther Hacker
Credit: N/A
Assignment: Birthday Problem

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = int(datetime.today().day)
todayyear = int(datetime.today().year)

todaymonthname = month_name[todaymonth].lower()

name = input("Hello, what is your name? ")
month = input("Hi " + name + ", what is the name of the month you were born in? ")
month = month.lower()
day = int(input("And what day of the month were you born on, " + name + "? "))
year = int(input("And the year? "))

if month == "october" and day == 31:
    print("You were born on Halloween!")
    
else:
    if month == todaymonthname and day == todaydate:
        print("Happy birthday!")

    else:
        if month == "december" or month == "january" or month == "february":
            season = "winter"
        
        if month == "march" or month == "april" or month == "may":
            season = "spring"
            
        if month == "june" or month == "july" or month == "august":
            season = "summer"
        
        if month == "september" or month == "october" or month == "november":
            season = "fall"
        
        if year in range(1980, 1990):
            decade = "eighties"
            
        if year in range(1990, 2000):
            decade = "nineties"
        
        if year in range(2000, todayyear):
            decade = "two thousands"
            
        if year not in range(1980, todayyear):
            decade = "stone age"
        
        print(name + ", you are a " + season + " baby of the " + decade + ".")
