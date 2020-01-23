
# Problem
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
#
# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
#
# Sample Input
# 07:05:45PM
#
# Sample Output
# 19:05:45


#!/bin/python3

import os
import sys
import datetime
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    date = datetime.datetime.strptime(s,'%I:%M:%S%p')
    date = datetime.datetime.strftime(date,'%H:%M:%S')
    return str(date)


if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)