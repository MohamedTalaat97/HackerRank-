#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0]*n
    for query in queries:
        a,b,k = query[0]-1, query[1]-1,query[2]
        array [a:b+1] = [x+k for x in array[a:b+1]]
    return max(array)
        
if __name__ == '__main__':


    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)
