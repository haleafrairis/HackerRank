# Task
# Given a string,S, of length N that is indexed from 0 to N-1 , 
# print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).
# Note: 0 is considered to be an even index.

# Example
# adbecf
# Print abc def

# Input Format
# The first line contains an integer, T (the number of test cases).
# Each line i of the T subsequent lines contain a string, S.

# Constraints
# 1 <= T <= 10
# 2 <= length of S <= 10000

# Output Format
# For each String S_j (where 0 <= j <= T-1 ), print S_j's even-indexed characters, followed by a space, followed by S_j's odd-indexed characters.

# Sample Input
# 2
# Hacker
# Rank

# Sample Output
# Hce akr
# Rn ak

# Code 

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(0,T):
    S = input()
    print(f"{S[0::2]} {S[1::2]}")
