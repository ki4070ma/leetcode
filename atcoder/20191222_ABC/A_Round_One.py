#!/usr/bin/python3

from sys import stdin


for _ in range(2):
    l = [1, 2, 3]
    A = int(stdin.readline().rstrip())
    B = int(stdin.readline().rstrip())
    l.remove(A)
    l.remove(B)
    print(l[0])
