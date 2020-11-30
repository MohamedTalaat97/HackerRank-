#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    #
    # Write your code here.
    #
    print(s[-2:], s[0:2])
    if s[-2:] == 'AM' and s[0:2] != '12':
        return s[0:len(s)-2]
    elif s[-2:] == 'AM' and s[0:2] == '12':
        return '00' + s[2:len(s)-2]
    elif s[-2:] == 'PM' and s[0:2] == '12':
        return s[0:len(s)-2]
    else:
        hour = int(s[0:2])
        hour += 12
        return str(hour)+s[2:len(s)-2]


if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
