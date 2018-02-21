#!/bin/python3

import sys


def largest_permutation(k, arr):
    arr_len = len(arr)
    limit = arr_len-k

    result = list(range(arr_len, limit, -1)) + arr[k:]

    if k >= len(arr):
        return sorted(arr, reverse=True)

    for i in range(k, arr_len):
        if arr[i] > limit:
            result[i] = arr[i]-1

    return result


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))

    result = largest_permutation(k, arr)
    print (" ".join(map(str, result)))


