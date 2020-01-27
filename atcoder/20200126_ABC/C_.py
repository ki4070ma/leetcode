#!/usr/bin/python3

from sys import stdin

for _ in range(3):
    N, K = map(int, input().rstrip().split())
    Hs = [int(x) for x in input().rstrip().split()]

    # print(Hs)
    if K == 0:
        print(sum(Hs))
    else:
        print(sum(sorted(Hs)[:-K]))
