#!/bin/python3

import math
import os
import random
import re
import sys


class Node:
    def __init__(self, score, left, right):
        self.score = score
        self.left = left
        self.right = right


class Tree:
    def __init__(self, array):
        sorted_array = sorted(list(set(array)), reverse=True)
        input_length = len(sorted_array)
        root_rank = math.ceil(input_length / 2) - 1

        self.root = Node(sorted_array[root_rank], None, None)
        self.root_rank = root_rank + 1

        del sorted_array[root_rank]

        for i in range(len(sorted_array)):
            self.append(self.root, sorted_array[i])

    def append(self, node, score):
        if score == node.score:
            return

        if score > node.score:
            if node.right is None:
                node.right = Node(score, None, None)
            else:
                if score < node.right.score:
                    new_right = Node(score, None, node.right)
                    node.right = new_right
                else:
                    self.append(node.right, score)

        if score < node.score:
            if node.left is None:
                node.left = Node(score, None, None)
            else:
                if score > node.left.score:
                    new_left = Node(score, node.left, None)
                    node.left = new_left
                self.append(node.left, score)

    def get_rank(self, score):
        return self.__get_rank(self.root, self.root_rank, score)

    def __get_rank(self, node, rank, score):
        if score == node.score:
            return rank

        if score > node.score:
            if node.right is not None:
                return self.__get_rank(node.right, rank - 1, score)
            else:
                return rank

        if score < node.score:
            if node.left is not None:
                return self.__get_rank(node.left, rank + 1, score)
            else:
                return rank + 1


def climb_ladder(scores, alice):
    tree = Tree(scores)
    res = []

    for i in range(len(alice)):
        res.append(tree.get_rank(alice[i]))

    return res


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))

    result = climb_ladder(scores, alice)

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')
    #fptr.close()
