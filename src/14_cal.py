"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


def month_year():
    while True:
        try:
            calendar.setfirstweekday(calendar.SUNDAY)
            today = datetime.today()
            yyyy = int(input('Input year as a four digit number or press Enter for current year:') or today.year)
            mm = int(input('Input month as a two digit number or press Enter for current month:') or today.month)
            print(calendar.month(yyyy, mm))
        except ValueError:
            print("Please use integer numbers and not a letters for input!")
            break
        else:
            print(f"This is the calendar for {mm} {yyyy}")
            break


month_year()



