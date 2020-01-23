
# Problem
#
# You are choreographing a circus show with various animals.
# For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
#
# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show.
# If it is possible, return YES, otherwise return NO.
#
# For example, kangaroo 1 starts at x1=2 with a jump distance v1=1 and kangaroo 2 starts at x2=1 with a jump distance of v2=2.
# After one jump, they are both at x=3, (x1+v1=2+1,x2+v2=1+2 ), so our answer is YES.
#
# Sample Input 0
# 0 3 4 2
#
# Sample Output 0
# YES
#
# Sample Input 1
# 0 2 5 3
#
# Sample Output 1
# NO

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (v1 > v2):
        remainder = (x1 - x2) % (v2 - v1)
        if remainder == 0:
            return "YES"
    return "NO"


if __name__ == '__main__':
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)