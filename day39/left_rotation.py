#!/bin/python3


def rotate_left(a, d):
    return a[d:] + a[:d]


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))

    result = rotate_left(a, d)

    print(' '.join(map(str, result)))
    print('\n')
