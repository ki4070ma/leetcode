#!/usr/bin/python3

from sys import stdin

for _ in range(1):
    N = int(stdin.readline().rstrip())
    S, T = map(str, stdin.readline().rstrip().split())
    ret = ''
    for i in range(N):
        ret += S[i]
        ret += T[i]
    print(ret)

