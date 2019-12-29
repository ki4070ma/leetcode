#!/usr/bin/python3

from sys import stdin

for _ in range(5):
    A, B, K = map(int, stdin.readline().rstrip().split())

    A = A - K
    if A < 0:
        B = B + A
        A = 0
    if B < 0:
        B = 0

    print('{} {}'.format(A, B))


