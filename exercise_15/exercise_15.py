# Reading Files
from sys import argv

script, filename = argv
#python exercise_15.py exercise_15.py

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename agian:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())