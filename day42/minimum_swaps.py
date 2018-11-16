#!/bin/python3


def minimum_swaps(q):
    count = 0
    sorted = list(range(1, len(q)+1))

    while q != sorted:
        min_index = 0
        max_index = 0
        length = len(q)

        for i in range(length):
            if q[i] != i+1:
                min_index = i
                break

        for j in range(length):
            if q[j] == min_index + 1:
                max_index = j
                break

        tmp = q[max_index]
        q[max_index] = q[min_index]
        q[min_index] = tmp
        count += 1
    return count


if __name__ == '__main__':
    x = int(input())
    arr = list(map(int, input().rstrip().split()))

    res = minimum_swaps(arr)
    print(str(res) + '\n')
