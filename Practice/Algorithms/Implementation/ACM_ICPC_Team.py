#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic): 

    res = []

    for i in range(1, n):

        for k in range(i+1, n+1):
            count = 0            
            first_member_topics = topic[i-1]
            second_member_topics = topic[k-1]
            for item, letter in enumerate(first_member_topics):                
                if letter == "1" or second_member_topics[item] == "1" :
                    count+=1            
            res.append(count)


    result = [max(res), res.count(max(res))]
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
