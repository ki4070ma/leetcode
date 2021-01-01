#!/usr/bin/python3

from sys import stdin

for _ in range(4):
    H, N = map(int, input().rstrip().split())
    As = [int(x) for x in input().rstrip().split()]
    total_attack = sum(As)
    if H > total_attack:
        print("No")
    else:
        print("Yes")
