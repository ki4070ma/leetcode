#!/usr/bin/python3

from sys import stdin

for _ in range(3):
    H, A = map(int, input().rstrip().split())
    # print(f'H: {H}, A: {A}')
    ret = H / A if H % A == 0 else H // A + 1
    print(int(ret))
