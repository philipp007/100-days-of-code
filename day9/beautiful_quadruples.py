#!/bin/python3

import itertools


def xor(a, b, c, d):
    return a ^ b ^ c ^ d


def get_key(a, b, c, d):
    return ''.join(str(x) for x in sorted([a, b, c, d]))


A,B,C,D = input().strip().split(' ')
A,B,C,D = [int(A),int(B),int(C),int(D)]

lst = sorted([A, B, C, D])
A, B, C, D = lst

count = 0
cacheA = {}
cacheB = {}
cacheC = {}

for i in range(1, A+1):
    for j in range(i, B+1):
        cacheA[(i, j)] = i ^ j

for k in range(1, C+1):
    for l in range(C, D+1):
        cacheB[(k, l)] = k ^ l

for a in cacheA.values():
    for b in cacheB.values():
        if a ^ b != 0:
            count = count + 1


print(count)