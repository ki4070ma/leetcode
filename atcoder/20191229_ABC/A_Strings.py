#!/usr/bin/python3

from sys import stdin

for _ in range(2):
    S, T = stdin.readline().rstrip().split()
    print(T + S)
