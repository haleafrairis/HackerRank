# Task
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), 
# and tax percent (the percentage of the meal price being added as tax) for a meal, 
# find and print the meal's total cost. Round the result to the nearest integer.

# Function Description
# Complete the solve function in the editor below.
# solve has the following parameters:
# int meal_cost: the cost of food before tip and tax
# int tip_percent: the tip percentage
# int tax_percent: the tax percentage
# Returns The function returns nothing. Print the calculated value, rounded to the nearest integer.

# Input Format
# There are 3 lines of numeric input:
# The first line has a double, mealCost (the cost of the meal before tax and tip).
# The second line has an integer, tipPercent (the percentage of mealCost being added as tip).
# The third line has an integer, taxPercent (the percentage of mealCost being added as tax).

# Sample Input
# 12.00
# 20
# 8

# Sample Output
# 15

# Code 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = (meal_cost/100)*tip_percent
    tax = (meal_cost/100)*tax_percent
    total_cost = meal_cost + tip +tax
    result = round(total_cost)
    print(result)
    

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
