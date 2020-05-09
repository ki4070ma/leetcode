#!/usr/bin/python3

for _ in range(2):
    N, K = map(int, input().rstrip().split())
    # print(N, K)
    l = []
    for _ in range(K):
        d = input().rstrip()
        As = [int(x) for x in input().rstrip().split()]
        l.extend(As)
        # print(d, As)
    print(N - len(set(l)))
