#!/usr/bin/python3

from sys import stdin

for _ in range(3):
    S = int(stdin.readline().rstrip())

    if S % 2 == 0:
        print(1 / 2)
    elif S % 2 == 1:
        print((int(S / 2) + 1) / S)
