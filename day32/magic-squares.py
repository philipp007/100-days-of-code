#!/bin/python3


def cost(source, target):
    result = 0
    for i in range(3):
        for j in range(3):
            result += abs(source[i][j] - target[i][j])

    return result


def cost_sq1(s):
    square = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    return cost(s, square)


def cost_sq2(s):
    square = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
    return cost(s, square)


def cost_sq3(s):
    square = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    return cost(s, square)


def cost_sq4(s):
    square = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
    return cost(s, square)


def cost_sq5(s):
    square = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    return cost(s, square)


def cost_sq6(s):
    square = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
    return cost(s, square)


def cost_sq7(s):
    square = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
    return cost(s, square)


def cost_sq8(s):
    square = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    return cost(s, square)


def minimum_cost(s):
    costs = [cost_sq1(s), cost_sq2(s), cost_sq2(s), cost_sq3(s), cost_sq4(s), cost_sq5(s), cost_sq6(s), cost_sq7(s), cost_sq8(s)]
    return min(costs)


if __name__ == '__main__':
    arr = []

    for _ in range(3):
        arr.append(list(map(int, input().rstrip().split())))

    result = minimum_cost(arr)
    print(result)
