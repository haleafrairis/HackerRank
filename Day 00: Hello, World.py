# Task
# To complete this challenge, you must save a line of input from stdin to a variable, 
# print Hello, World. on a single line, and finally print the value of your variable on a second line.

# Input Format
# A single line of text denoting inputString (the variable whose contents must be printed).

# Output Format
# Print Hello, World. on the first line, and the contents of inputString on the second line.

# Sample Input:
# Welcome to 30 Days of Code!

# Sample Output
# Hello, World. 
# Welcome to 30 Days of Code!

# Code
# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
# TODO: Write a line of code here that prints the contents of input_string to stdout.
print(f'Hello, World.\n{input_string}')
