#!/usr/bin/python3

from sys import stdin

for _ in range(3):
    N, K, M = map(int, stdin.readline().rstrip().split())
    As = list(map(int, stdin.readline().rstrip().split()))

    print('N: {}, K: {}, M: {}'.format(N, K, M))
    print(As)

    X = M * N - sum(As)
    if X > K:
        print(-1)
    elif X < 0:
        print(0)
    else:
        print(X)
