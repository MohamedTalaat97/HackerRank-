#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the isBalanced function below.


def isBalanced(s):
    types = {
        '(': ')',
        ')': '(',
        '[': ']',
        ']': '[',
        '{': '}',
        '}': '{'}
    brackets = list(s)
    if len(brackets) % 2 != 0:
        return "NO"
    stack = deque()
    for bracket in brackets:
        if len(stack) == 0:
            stack.append(bracket)
            continue
        b = stack.pop()
        if types[bracket] != b or bracket not in ['{', '(', '[']:
            stack.append(b)
            stack.append(bracket)
    if len(stack) != 0:
        return "NO"
    return "YES"


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result)
