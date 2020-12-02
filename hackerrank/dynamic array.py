#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    twoDimensionalArray =[]
    lastAnswer = 0
    result = []
    for i in range(n):
        data = []
        twoDimensionalArray.append(data)

    for i in range(len(queries)):
        type = queries[i][0]
        x= queries[i][1]
        y =queries[i][2]
        if type == 1:
            index = (x^lastAnswer)%n
            twoDimensionalArray[index].append(y)

        else:
            index = (x^lastAnswer)%n
            lastAnswer = twoDimensionalArray[index][y%len(twoDimensionalArray[index])]
            result.append(lastAnswer)
        

    return result


if __name__ == '__main__':


    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print(result)