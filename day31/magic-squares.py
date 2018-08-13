#!/bin/python3

import math
import os
import random
import re
import sys


def fix_diagonal1(s):
    sum = s[0][0] + s[1][1] + s[2][2]
    diff = sum - 15

    if diff != 0:
        s[0][0] = s[0][0] - diff

    return abs(diff)


def fix_diagonal2(s):
    sum = s[0][2] + s[1][1] + s[2][0]
    diff = sum - 15

    if diff != 0:
        s[0][2] = s[0][2] - diff

    return abs(diff)


def form_magic_square(s):
    m = 15
    cost = 0

    cost += fix_diagonal1(s)
    cost += fix_diagonal2(s)
    # fix diagonals
    # fix rows
    # fix columns

    return cost


if __name__ == '__main__':
    arr = []

    for _ in range(3):
        arr.append(list(map(int, input().rstrip().split())))

    result = form_magic_square(arr)
    print(result)
