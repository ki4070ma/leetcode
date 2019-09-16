#!/usr/bin/python3

from sys import stdin


for _ in range(4):

    N, M = map(int, stdin.readline().rstrip().split())
    S = list(map(int, stdin.readline().rstrip().split()))
    import numpy

    for i in range(M):
        max_val = numpy.max(S)
        S[S.index(max_val)] = max_val / 2
    print(int(sum(S)))
