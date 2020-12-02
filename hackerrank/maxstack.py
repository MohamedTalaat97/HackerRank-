# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


# Complete the arrayManipulation function below.
def stackqueries(queries):
    stack = deque()
    maxi = {"max": 0, "count": 0}
    for query in queries:
        if query[0] == 1:
            x = query[1]
            stack.append(x)
            if x > maxi["max"]:
                maxi["max"] = x
                maxi["count"] = 1
            elif x == maxi["max"]:
                maxi["count"] += 1
        elif query[0] == 2:
            y = stack.pop()
            if y == maxi["max"]:
                maxi["count"] -= 1
                if maxi["count"] == 0:
                    maxi["max"] = 0

        else:
            print(maxi["max"])


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    queries = []

    for _ in range(n):
        queries.append(list(map(int, input().rstrip().split())))

    result = stackqueries(queries)
