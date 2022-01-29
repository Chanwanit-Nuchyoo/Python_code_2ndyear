"""
12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""

import calendar

user_input = input("Enter month and year : ")
m_y = [int(x) for x in user_input.split()]

print(calendar.month(m_y[1],m_y[0]))