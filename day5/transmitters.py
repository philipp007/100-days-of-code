#!/bin/python3

import sys

def createList(n):
    list = []
    for i in range(n):
        list.append([])

    return list


def hackerlandRadioTransmitters(x, k):
    covered = createList(len(x))
    count = 0
    x = sorted(x)
    stations = [x[0]]

    for i in x:
        diff = i - k

        if len(covered[count]) > 0 and diff > covered[count][0]:
            count = count + 1
            stations.append(i)

        if count > 0 and diff <= stations[count-1]:
            covered[count-1].append(i)
        else:
            covered[count].append(i)
            stations[count] = i

    length = len(stations)
    if count > 0 and stations[count] in covered[count - 1]:
        return length - 1
    return length


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
x = list(map(int, input().strip().split(' ')))
result = hackerlandRadioTransmitters(x, k)
print(result)
