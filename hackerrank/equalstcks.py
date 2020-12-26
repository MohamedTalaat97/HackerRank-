#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#


def equalStacks(h1, h2, h3):
    # Write your code here

    len1 = len(h1)
    len2 = len(h2)
    len3 = len(h3)

    if (len1 == len2 == len3 == 0):
        return 0

    while(1):
        sum1 = sum(h1)
        sum2 = sum(h2)
        sum3 = sum(h3)

        if (sum1 == sum2 == sum3):
            return sum1

        maxi = max([sum1, sum2, sum3])

        if maxi == sum1:
            h1.pop()
            continue
        if maxi == sum2:
            h2.pop()
            continue
        if maxi == sum3:
            h3.pop()
            continue


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = reverse(list(map(int, input().rstrip().split()))

    h2=list(map(int, input().rstrip().split()))

    h3=list(map(int, input().rstrip().split()))

    result=equalStacks(h1, h2, h3)

    print(result)
