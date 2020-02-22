#!/usr/bin/python3

for _ in range(3):
    N, K = map(int, input().rstrip().split())
    l = []
    mod = -1
    while N != 0:
        N, mod = divmod(N, K)
        # print(N, mod)
        l.append(mod)
    print(len(l))
