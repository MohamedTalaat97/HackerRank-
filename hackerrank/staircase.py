#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    str= []
    temp = ''
    for i in range(n):
        temp += '#'
    str.append(temp)
    for i in range(n):
        str.append(temp)
    j = 0    
    for i in range(n-1):
        str[i+1][0:j] = ' '
        j+=1  
    print(str)       
        
        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
