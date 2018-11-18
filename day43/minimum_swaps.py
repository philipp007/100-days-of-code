#!/bin/python3


def minimum_swaps(q):
    count = 0
    cache = {}
    length = len(q)

    for i in range(length):
        cache[q[i]] = i+1

    for i in range(len(q)):
        if q[i] != i+1:
            tmp = q[i]
            q[i] = i+1
            q[cache[i+1] - 1] = tmp
            cache[tmp] = cache[i+1]
            cache[i+1] = i+1
            count += 1

    return count


if __name__ == '__main__':
    x = int(input())
    arr = list(map(int, input().rstrip().split()))

    res = minimum_swaps(arr)
    print(str(res) + '\n')
