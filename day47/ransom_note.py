#!/bin/python3


def check_magazine(magazine, note):
    magazine_items = {}

    for i in range(len(magazine)):
        item = magazine[i]
        if item in magazine_items:
            magazine_items[item] += 1
        else:
            magazine_items[item] = 1

    for i in range(len(note)):
        item = note[i]
        if item not in magazine_items or magazine_items[item] <= 0:
            print("No")
            return
        else:
            magazine_items[item] -= 1
    print("Yes")


if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    magazine = input().rstrip().split()
    note = input().rstrip().split()

    check_magazine(magazine, note)
