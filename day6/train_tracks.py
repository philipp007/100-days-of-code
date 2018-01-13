#!/bin/python3

from collections import defaultdict


def merge_intervals(intervals):
    """
    A simple algorithm can be used:
    1. Sort the intervals in increasing order
    2. Push the first interval on the stack
    3. Iterate through intervals and for each one compare current interval
       with the top of the stack and:
       A. If current interval does not overlap, push on to stack
       B. If current interval does overlap, merge both intervals in to one
          and push on to stack
    4. At the end return stack
    """
    sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
    merged = []

    for higher in sorted_by_lower_bound:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            # test for intersection between lower and higher:
            # we know via sorting that lower[0] <= higher[0]
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = (lower[0], upper_bound)  # replace by merged interval
            else:
                merged.append(higher)
    return merged


def gridland_metro(n, m, tracks):
    rails = {}

    sum = 0

    for track in tracks:
        row_number = track[0]

        if row_number not in rails:
            rails[row_number] = [[track[1], track[2]]]
        else:
            rails[row_number].append([track[1], track[2]])

    for rail in rails.values():
        merged_intervals = merge_intervals(rail)

        for interval in merged_intervals:
            sum = sum + interval[1] - interval[0] + 1

    return m*n - sum


if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    track = []
    for track_i in range(k):
       track_t = [int(track_temp) for track_temp in input().strip().split(' ')]
       track.append(track_t)
    result = gridland_metro(n, m, track)
    print(result)
