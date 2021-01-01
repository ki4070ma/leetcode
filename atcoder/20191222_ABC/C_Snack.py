#!/usr/bin/python3

from sys import stdin

for _ in range(3):
    A, B = map(int, stdin.readline().rstrip().split())

    X = A * B

    # greatest_common_divisor
    if A < B:
        tmp = B
        B = A
        A = tmp

    r = A % B
    while r != 0:
        A = B
        B = r
        r = A % B

    print(int(X / B))
