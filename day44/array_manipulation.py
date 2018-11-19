#!/bin/python3

import math
import os
import random
import re
import sys


def array_manipulation(n, queries):
    arr = [0] * n

    for i in range(len(queries)):
        a, b, k = queries[i]
        arr[a-1:b] = [x + k for x in arr[a-1:b]]

    return max(arr)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []

    for i in range(m):
        print("item " + str(i) + " of " + str(m) + " added")
        queries.append(list(map(int, input().rstrip().split())))

    result = array_manipulation(n, queries)
    print(result)

    #fptr.write(str(result) + '\n')
    #fptr.close()