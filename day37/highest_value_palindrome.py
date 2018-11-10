#!/bin/python3

import math
import os
import random
import re
import sys


def highest_value_palindrome(s, n, k):
    arr = list(s)
    is_even = n % 2 == 0
    limit = int(n / 2) if is_even else int(n / 2) + 1
    counter = k

    for i in range(0, limit):
        first = int(arr[i])
        last = int(arr[n - i - 1])

        if first > last:
            arr[n - i - 1] = str(first)
            counter -= 1
        elif last > first:
            arr[i] = str(last)
            counter -= 1

    if counter < 0:
        return "-1"
    if counter >= 0:
        for i in range(0, limit):
            if arr[i] == '9' and arr[n-i-1] == '9':
                continue
            if counter >= 2 and arr[i] == s[i] and arr[n-i-1] == s[n-i-1]:
                arr[i] = arr[n-i-1] = '9'
                counter -= 2
            elif counter >= 1 and (arr[i] != s[i] or arr[n-i-1] != s[n-i-1]):
                arr[i] = arr[n-i-1] = '9'
                counter -= 1
    if counter == 0:
        return ''.join(arr)
    if counter >= 1:
        if is_even:
            return ''.join(arr)
        else:
            arr[int(n / 2)] = '9'
            return ''.join(arr)

    return ''.join(arr)


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    s = input()

    result = highest_value_palindrome(s, n, k)
    print(result + "\n")
