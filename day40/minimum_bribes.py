#!/bin/python3

import math
import os
import random
import re
import sys


def minimum_bribes(q):
    swap_counts = {}
    total_count = 0
    n = len(q)

    for i in range(n):
        for j in range(n-i-1):
            if q[j] > q[j+1]:
                tmp = q[j]
                q[j] = q[j+1]
                q[j+1] = tmp

                if tmp not in swap_counts:
                    swap_counts[tmp] = 0
                swap_counts[tmp] += 1
                total_count += 1

                if swap_counts[tmp] > 2:
                    return -1

    return total_count


if __name__ == '__main__':
    t = int(input())
    bribes = []

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        bribes.append(minimum_bribes(q))

    for bribe in bribes:
        if bribe == -1:
            print('Too chaotic')
        else:
            print(bribe)
