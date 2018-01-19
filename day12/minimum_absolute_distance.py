#!/bin/python3
import math


def minimumAbsoluteDifference(n, arr):
    min = math.inf
    sorted_arr = list(sorted(arr))

    for i in range(n-1):
        distance = math.fabs(sorted_arr[i] - sorted_arr[i+1])
        if distance < min:
            min = distance

    return int(min)


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)
