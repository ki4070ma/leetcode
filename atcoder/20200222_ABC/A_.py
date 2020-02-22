#!/usr/bin/python3

for _ in range(2):
    N, R = map(int, input().rstrip().split())
    if N < 10:
        print(R + 100 * (10 - N))
    else:
        print(R)
