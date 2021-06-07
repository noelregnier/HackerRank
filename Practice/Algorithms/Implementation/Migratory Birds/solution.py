#https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys



def migratoryBirds(arr):
    s = set(arr)
    if arr == s: return min(arr)
    else:
        li = [(arr.count(i), i) for i in s]
        res = min([i[1] for i in li if i[0]==max(y[0] for y in li)])
        return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
