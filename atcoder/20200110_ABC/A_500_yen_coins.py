#!/usr/bin/python3

from sys import stdin

for _ in range(3):
    K, X = map(int, stdin.readline().rstrip().split())
    ret = "Yes" if K * 500 >= X else "No"
    print(ret)
