#!/usr/bin/python3

from sys import stdin

for _ in range(3):
    # print('***')
    N, K, Q = map(int, stdin.readline().rstrip().split())
    results = {}
    for i in range(N):
        results[str(i + 1)] = 0
    # print(results)
    for i in range(Q):
        S = stdin.readline().rstrip()
        results[S] += 1
    for i in range(N):
        if K - (Q - results[str(i + 1)]) > 0:
            print("Yes")
        else:
            print("No")
