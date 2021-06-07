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
        counts = {}
        for name in arr:
            counts[name] = counts.get(name, 0) + 1
        res = min([k for k,v in counts.items() if v == max(counts.values())])
        return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
