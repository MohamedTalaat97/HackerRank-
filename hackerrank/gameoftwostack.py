#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#


def twoStacks(x, a, b):
    #
    # Write your code here.
    #
    a.reverse()
    b.reverse()
    sumx = 0
    turn = 0
    moves = 0
    while sumx < x:
        if len(a) > 0:
            one = a.pop()
        else:
            one = 0
        if len(b) > 0:
            two = b.pop()
        else:
            two = 0
        if one >= two:
            turn = 1
            b.append(two)
        else:
            turn = 2

            a.append(one)

        if turn == 1:
            if sumx + one <= x:
                sumx += one
                moves += 1
            else:
                if sumx+two <= x:
                    sumx += two
                    moves += 1
                    b.pop()

        if turn == 2:
            if sumx + two <= x:
                sumx += two
                moves += 1
            else:
                if sumx+one <= x:
                    sumx += one
                    moves += 1
                    a.pop()
    return moves-1


if __name__ == '__main__':

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        print(result)
