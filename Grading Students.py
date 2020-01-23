
# Problem

# HackerLand University has the following grading policy:
#
# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:
#
# If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
# For example, 84 will be rounded to 85 but 29 will not be rounded because the rounding would result in a number that is less than 40.
#
# Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    new_grades = []
    for value in grades:
        score = int(value/5)
        next_multiple = (score + 1) * 5
        if(value < 38):
            new_grades.append(value)
        elif(next_multiple - value < 3):
            new_grades.append(next_multiple)
        else:
            new_grades.append(value)

    return new_grades


if __name__ == '__main__':

    # Sample input
    # 2
    # 44
    # 29
    #
    # Sample Output
    # [45, 29]
    
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)