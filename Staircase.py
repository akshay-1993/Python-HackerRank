
# Problem
# Consider a staircase of size : n = 4
#
#    #
#   ##
#  ###
# ####
# Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
#
# Write a program that prints a staircase of size n.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1, n+1):
        print(' '*(n-i)+"#"*i)

if __name__ == '__main__':
    n = int(input())

    staircase(n)