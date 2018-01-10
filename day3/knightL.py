#!/bin/python3

import sys
from queue import Queue


def push_knight_position(curr, a, b, bfs, visited):
    next_a = curr[0] + a
    next_b = curr[1] + b

    if [next_a, next_b] not in visited:
        bfs.put([next_a, next_b, curr[2]+1])
        visited.append([next_a, next_b])


def minimum_moves(a, b, n):
    visited = [[0, 0]]
    bfs = Queue()
    bfs.put([0, 0, 0])

    while bfs.qsize() > 0:
        curr = bfs.get()

        if curr[0] == n-1 and curr[1] == n-1:
            return curr[2]

        if curr[0] < 0 or curr[1] < 0 or curr[0] >= n or curr[1] >= n:
            continue

        push_knight_position(curr, -a, -b, bfs, visited)
        push_knight_position(curr, -a, b, bfs, visited)
        push_knight_position(curr, -b, -a, bfs, visited)
        push_knight_position(curr, -b, a, bfs, visited)
        push_knight_position(curr, a, -b, bfs, visited)
        push_knight_position(curr, a, b, bfs, visited)
        push_knight_position(curr, b, -a, bfs, visited)
        push_knight_position(curr, b, a, bfs, visited)

    return -1


def print_line(values):
    print(' '.join(str(item) for item in values))


n = int(input().strip())

cache = []

for i in range(n-1):
    cache.append([])
    for j in range(n-1):
        try:
            val = cache[j][i]
            cache[i].append(cache[j][i])
        except IndexError:
            cache[i].append(minimum_moves(i+1, j+1, n))

    print_line(cache[i])