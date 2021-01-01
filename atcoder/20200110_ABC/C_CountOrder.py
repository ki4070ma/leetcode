#!/usr/bin/python3

from sys import stdin

for _ in range(3):
    N = int(stdin.readline().rstrip())
    P = map(int, stdin.readline().rstrip().split())
    Q = map(int, stdin.readline().rstrip().split())

    import itertools

    l = list(itertools.permutations(list(range(1, N + 1))))
    a = l.index(tuple(P))
    b = l.index(tuple(Q))
    print(abs(a - b))
