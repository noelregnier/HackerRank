# https://www.hackerrank.com/challenges/between-two-sets/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def getTotalX(a, b):
    max_a = max(a)
    min_b = min(b)
    candidates = [max_a+i for i in range(0, min_b+1, max_a)]    
    number = 0
    for k in candidates:
        li = [k%i if i<=max_a else i%k for i in a+b]        
        if max(li)==0: number+=1
    return number

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
