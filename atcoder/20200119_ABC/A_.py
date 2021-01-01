#!/usr/bin/python3

for _ in range(3):
    N, M = map(int, input().rstrip().split())
    if N == M:
        print("Yes")
    else:
        print("No")
