# Task
# You are given two integer arrays of size NXP and MXP ( N&M  are rows, and P is the column). Your task is to concatenate the arrays along axis 0.

# Input Format
# The first line contains space separated integers N, M and P.
# The next N lines contains the space separated elements of the P columns.
# After that, the next M lines contains the space separated elements of the P columns.

# Output Format
# Print the concatenated array of size (N + M) X P.

# Sample Input
# 4 3 2
# 1 2
# 1 2 
# 1 2
# 1 2
# 3 4
# 3 4
# 3 4

# Sample Output
# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]
#  [3 4]
#  [3 4]
#  [3 4]]

# Code

import numpy
list_1 =[]
list_2 =[]
input_ = input()
N = int(input_.split()[0])
M = int(input_.split()[1])
P = int(input_.split()[2])
for _ in range(N):
    list_1.append(input().split())
    array_1 = numpy.array(list_1,int)
for _ in range(M):
    list_2.append(input().split())
    array_2 = numpy.array(list_2,int)
print(numpy.concatenate((array_1, array_2), axis = 0))
