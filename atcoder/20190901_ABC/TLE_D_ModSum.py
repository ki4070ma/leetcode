#!/usr/bin/python3

from sys import stdin

for _ in range(1):
    N = int(stdin.readline().rstrip())
    list_N = list(range(1, N + 1))

    ret = 0
    for i in list_N:
        val = sum([x % i for x in list_N])
        if ret < val:
            ret = val

    print(ret)
