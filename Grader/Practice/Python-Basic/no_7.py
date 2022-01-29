"""
7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java
"""

filename = input("Enter filename : ")
output = filename.split(".")

print("Extension : "+ output[-1])