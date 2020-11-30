#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.


def staircase(n):
    s = []
    temp = ''
    for i in range(n):
        temp += '#'
    s.append(temp)
    for i in range(n-1):
        s.append(temp)
    j = 1

    print(s)
    for i in range(n-1):
        k = list(s[i+1])
        k[0:j] = ' '*(j-0)
        j += 1
        s[i+1] = k
    for string in reversed(s):
        print(''.join(string), '\n')


if __name__ == '__main__':
    n = int(input())

    staircase(n)
