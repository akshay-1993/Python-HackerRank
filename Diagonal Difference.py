#
# Problem
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#
# For example, the square matrix  is shown below:
#
# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17.
# Their absolute difference is |15 - 17| = 2.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    first_diagonal = sum(arr[i][i] for i in range(n))
    second_diagonal = sum(arr[i][n-i-1] for i in range(n))
    return abs(first_diagonal - second_diagonal)


if __name__ == '__main__':
    # Input format
    # 3
    # 1 2 3
    # 4 5 6
    # 9 8 9
    #
    # output = 2
    #
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
