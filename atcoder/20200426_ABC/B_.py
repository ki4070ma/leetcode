#!/usr/bin/python3

for _ in range(2):
    A, B, C, D = map(int, input().rstrip().split())
    for _ in range(100):
        C -= B
        if C < 1:
            print('Yes')
            break
        A -= D
        if A < 1:
            print('No')
            break
