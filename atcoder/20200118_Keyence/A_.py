#!/usr/bin/python3

for _ in range(3):
    H = int(input().rstrip())
    W = int(input().rstrip())
    N = int(input().rstrip())
    longer = max(H, W)
    if N % longer == 0:
        print(N // longer)
    else:
        print(N // longer + 1)
