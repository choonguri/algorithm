#!/bin/python3

# https://www.hackerrank.com/challenges/time-conversion/problem

import sys

def timeConversion(s):
    # Complete this function
    h = s[:2]
    am_pm = s[-2:]
    t = s[2:-2]
    if am_pm == 'PM':
        hh = int(h)+12
        if hh == 24:
            hh = 12
        return str(hh)+t
    else:
        hh = int(h)
        if hh == 12:
            hh = 0

        if hh < 10:
            hh_str = '0' + str(hh)
        else:
            hh_str = str(hh)
        return hh_str+t

s = input().strip()
result = timeConversion(s)
print(result)
