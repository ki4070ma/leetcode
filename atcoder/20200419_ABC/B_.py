#!/usr/bin/python3

for _ in range(4):
    N, M = map(int, input().rstrip().split())
    As = [int(x) for x in input().rstrip().split()]
    # print(N, M)
    # print(As)
    ret = N - sum(As)
    if ret < 0:
        print(-1)
    else:
        print(ret)
