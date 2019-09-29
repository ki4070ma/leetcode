#!/usr/bin/python3

from sys import stdin

for _ in range(3):
    N, K = map(int, stdin.readline().rstrip().split())
    Hs = map(int, stdin.readline().rstrip().split())
    print(len([x for x in Hs if x >= K]))
