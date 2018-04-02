#!/bin/python3

# https://www.hackerrank.com/challenges/sherlock-and-minimax/problem

import sys


def sherlockAndMinimax(arr, p, q):
    # Complete this function
    diff_arr = []
    p_diff_arr = []

    for item in arr:
        diff_arr.append(item - p)

    for _ in range(q - p + 1):
        p_diff_arr.append(min([abs(x) for x in diff_arr]))
        diff_arr = [y - 1 for y in diff_arr]

    return p_diff_arr.index(max(p_diff_arr)) + p


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    p, q = input().strip().split(' ')
    p, q = [int(p), int(q)]
    result = sherlockAndMinimax(arr, p, q)
    print(result)
