# Context
# Given a 6 x 6 2D Array, A:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:
# a b c
#   d
# e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

# Task
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

# Example
# In the array shown above, the maximum hourglass sum is 7 for the hourglass in the top left corner.

# Input Format
# There are 6 lines of input, where each line contains 6 space-separated integers that describe the 2D Array A.

# Constraints
# -9 <= A[i][j] <= 9
# 0 <= i,j <= 5

# Output Format
# Print the maximum hourglass sum in A.

# Sample Input
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

# Sample Output
# 19

# Explanation

# A contains the following hourglasses:

# 1 1 1   1 1 0   1 0 0   0 0 0
#   1       0       0       0
# 1 1 1   1 1 0   1 0 0   0 0 0

# 0 1 0   1 0 0   0 0 0   0 0 0
#   1       1       0       0
# 0 0 2   0 2 4   2 4 4   4 4 0

# 1 1 1   1 1 0   1 0 0   0 0 0
#   0       2       4       4
# 0 0 0   0 0 2   0 2 0   2 0 0

# 0 0 2   0 2 4   2 4 4   4 4 0
#   0       0       2       0
# 0 0 1   0 1 2   1 2 4   2 4 0

# The hourglass with the maximum sum (19) is:
# 2 4 4
#   2
# 1 2 4

# Code 

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
list_ = []
for i in range(0,4):
    for j in range(0,4):
        result = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        list_.append(result)  
print(max(list_))












