#!/bin/python3

import math
import os
import random
import re
import sys


def climbingLeaderboard(ranked, player):
    result =[]
    player = player

    ranked = set(ranked)
    leaders = len(ranked)    
    ranked = [(k,i+1) for i,k in enumerate(sorted(ranked, reverse=True))]
    # print(ranked)

    #number the player list
    player = [(k, i+1) for i, k in enumerate(player)]
    player = sorted(player, key = lambda a : a[0], reverse=True)
    # print(player)

    #comparison
    p = player.pop(0)
    r = ranked.pop(0)
    score = 0
    while p and r:
        if p[0] >= r[0]:
            result.append((r[1], p[1]))
            try:
                p = player.pop(0)
            except:
                p = 0
        else:
            try:
                r = ranked.pop(0)
            except:
                score=r[1]+1
                r=0


    while p:
        result.append((score, p[1]))
        try:
            p = player.pop(0)
        except:
            p = 0


   
    result.sort(key=lambda a: a[1])
    result = [i[0] for i in result]
    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    print(result)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    
    fptr.close()
