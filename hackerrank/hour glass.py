#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    i = 0
    j = 0
    x = []
    for row in range(16):
        if i > 3:
            break
        if j == 4:
            i += 1
            j = 0
        x.append(sum(arr[i][j:j+3]) + sum(arr[i+2][j:j+3]) +
                 + arr[i+1][j+1])
        j += 1
    return max(x)


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
