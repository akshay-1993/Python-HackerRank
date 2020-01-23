# Problem
# Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.
#
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
#
# For example, given the array  there are  elements, two positive, two negative and one zero. Their ratios would be ,  and . It should be printed as
#
# 0.400000
# 0.400000
# 0.200000

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    array_length = len(arr)
    for value in arr:
        if value > 0:
            positive_count += 1
        elif value < 0:
            negative_count += 1
        elif value == 0:
            zero_count += 1
    print(positive_count/array_length,"\n",negative_count/array_length,"\n",zero_count/array_length)

if __name__ == '__main__':

    # Sample input
    # 5
    # 1 1 0 -1 -1
    #
    # Output
    # 0.4
    # 0.4
    # 0.2

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)