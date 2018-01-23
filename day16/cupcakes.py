#!/bin/python3


def cake_walk(calories):
    miles = 0
    sorted_calories = sorted(calories)
    count = len(sorted_calories)

    for i in range(count):
        miles += sorted_calories[count-i-1] * (2**i)

    return miles


if __name__ == "__main__":
    n = int(input().strip())
    calories = list(map(int, input().strip().split(' ')))
    result = cake_walk(calories)
    print(result)
