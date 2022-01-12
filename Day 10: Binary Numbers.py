# Task
# Given a base-10 integer,n, convert it to binary (base-2). 
# Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
# When working with different bases, it is common to show the base as a subscript.

# Input Format
# A single integer, n.

# Constraints
# 1 <= n <= 10^6

# Output Format
# Print a single base-10 integer that denotes the maximum number of consecutive 1's in the binary representation of n.

# Sample Input 1
# 5
# Sample Output 1
# 1

# Sample Input 2
# 13
# Sample Output 2
# 2

# Code
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
list_ = []
t = 0
while n > 0:
    if n % 2 == 1:
        t += 1
        list_.append(t)
    if n % 2 == 0:
        t = 0
    n = n // 2
print(max(list_))
