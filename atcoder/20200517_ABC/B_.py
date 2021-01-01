#!/usr/bin/python3

for _ in range(2):
    K = int(input().rstrip())
    S = input().rstrip()
    if len(S) > K:
        print(S[:K] + "...")
    else:
        print(S)
