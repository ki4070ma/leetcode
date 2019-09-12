#!/usr/bin/python3

from sys import stdin

for _ in range(4):
    N, K = map(int, stdin.readline().rstrip().split())
    S = list(stdin.readline().rstrip())

    print(N, K, S)

    data = []
    base = S[0]
    count = 1
    for a in S[1:]:
        # print(a)
        if base == a:
            count += 1
        else:
            base = a
            data.append(count)
            count = 1
    data.append(count)
    print(data)
