#!/bin/python3

from collections import deque


def absolute_permutation(n, k):
    if k == 0:
        return list(range(1, n+1))

    if n % k != 0 or int(n / k) % 2 != 0:
        return [-1]

    items = list(range(1, n+1))
    pair_length = k * 2
    pair_count = int(n / pair_length)
    result = []

    for i in range(0, pair_count):
        start_index = i * pair_length
        deq = deque(items[start_index:start_index + pair_length])
        deq.rotate(k)
        result.extend(list(deq))

    return result


if __name__ == '__main__':
    t = int(input())
    results = []

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        result = absolute_permutation(n, k)
        results.append(' '.join(map(str, result)))

    for i in range(len(results)):
        print(results[i])
