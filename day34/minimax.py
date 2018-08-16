#!/bin/python3
def mini_max_sum(arr):
    sorted_array = sorted(arr)
    min = sum(sorted_array[0:4])
    max = sum(sorted_array[1:])

    print(min, max, sep=" ")


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    mini_max_sum(arr)
