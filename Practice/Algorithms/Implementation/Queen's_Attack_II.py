#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):

    steps = 0
    if k:
        obs = tuple(tuple(i) for i in obstacles)
    else:
        obs = (0, 0),
    # print(obs)

    # horizontal
    horizontal_obstacles = [i for i in obs if i[0] == r_q]
    try:
        right_min_obstacle_column = [i for i in sorted(horizontal_obstacles) if i[1] > c_q][0][1]
        steps += right_min_obstacle_column - c_q -1
    except:
        steps += n - c_q
    try:
        left_max_obstacle_column = [i for i in sorted(horizontal_obstacles) if i[1] < c_q][-1][1]
        steps += c_q - left_max_obstacle_column -1
    except:
        steps += c_q - 1


    #vertical
    vertical_obstacles = [i for i in obs if i[1] == c_q]
    try:
        upper_min_obstacle_row = [i for i in sorted(vertical_obstacles) if i[0] > r_q][0][0]
        steps += upper_min_obstacle_row - r_q -1
    except:
        steps += n - r_q
    try:
        lower_max_obstacle_row = [i for i in sorted(vertical_obstacles) if i[0] < r_q][-1][0]
        steps += r_q - lower_max_obstacle_row - 1
    except:
        steps += r_q - 1

    #diagonal down_to_up
    diagonal_1_obstacles = [i for i in obs if i[0] - r_q == i[1] - c_q]
    try:
        up_min_diag_1_obstacle = [i for i in sorted(diagonal_1_obstacles) if i[0] > r_q and i[1] > c_q][0][0]
        steps += up_min_diag_1_obstacle - r_q -1
    except:
        if r_q == n or c_q == n:
            pass
        else:
            max_num = max([r_q, c_q])
            steps += n - max_num
    try:
        down_max_diag_1_obstacle = [i for i in sorted(diagonal_1_obstacles) if i[0] < r_q and i[1] < c_q][-1][0]
        steps += r_q - down_max_diag_1_obstacle - 1
    except:
        if r_q == 1 or c_q == 1:
            pass
        else:
            min_num = min([r_q, c_q])
            steps += min_num - 1

    #diagonal_up_to_down
    diagonal_2_obstacles = [i for i in obs if i[0] - r_q == -(i[1] - c_q)]
    try:
        up_min_diag_2_obstacle = [i for i in sorted(diagonal_2_obstacles) if i[0] > r_q][0][0]
        steps += up_min_diag_2_obstacle - r_q - 1
    except:
        if r_q == n or c_q == 1:
            pass
        else:
            # steps += n - r_q
            min_n = min([n - r_q, c_q - 1])
            steps += min_n
    try:
        down_max_diag_2_obstacle = [i for i in sorted(diagonal_2_obstacles) if i[0] < r_q][-1][0]
        steps += r_q - down_max_diag_2_obstacle - 1
    except:
        if r_q == 1 or c_q == n:
            pass
        else:
            # steps += n -c_q
            min_n = min([n - c_q, r_q - 1])
            steps += min_n

    # print(steps)

    return steps



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
