#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr):
    size = len(arr)
    plus, zero, minus = 0, 0, 0
    for element in arr:
        if element > 0:
            plus += 1
        elif element < 0:
            minus += 1
        else:
            zero += 1
    return round(plus/size, 6), round(minus/size, 6), round(zero/size, 6)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(plusMinus(arr))
