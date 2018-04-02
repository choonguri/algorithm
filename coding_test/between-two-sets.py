#!/bin/python3
# https://www.hackerrank.com/challenges/between-two-sets/problem

import sys


def getTotalX(a, b):
    # Complete this function
    # 최소공배수

    if max(a) > min(b):
        return  0

    biggest_a = max(a)
    while True:
        ok = True
        for i in a:
            if biggest_a % i != 0:
                ok = False
                break

        if ok:
            break
        biggest_a += 1

    cnt = 0
    ss = biggest_a
    while True:
        ok = True
        for j in b:
            if j % ss != 0:
                ok = False
                break
        ss = ss + biggest_a

        if ok:
            cnt += 1

        if b[0] < ss:
            break

    return cnt


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
