#!/bin/python3


def anagrams(s):
    dict = {}
    length = len(s)
    prevs = {}

    for i in range(length):
        for j in range(i+1, length+1):
            key = ''.join(sorted(s[i:j]))

            if key in dict:
                next_val = prevs[key] + 1
                dict[key] += next_val
                prevs[key] = next_val
            else:
                dict[key] = 0
                prevs[key] = 0

    return sum(dict.values())


if __name__ == '__main__':
    q = int(input())
    result = []

    for q_itr in range(q):
        s = input()
        result.append(anagrams(s))

    for i in range(len(result)):
        print(result[i])
