"""
Exercise 1 (and Solution)
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""
from datetime import date

name = input("Enter your name: ")
print("Your name is " + name)
age = int(input("Enter your age: "))
year_left = 100 - age
today = date.today()
str = name + " will turns 100 years old in " + str(today.year + year_left) + "\n"
print(str)
n = int(input("Enter a number: "))
print(str * n)