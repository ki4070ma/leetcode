#!/usr/bin/python3

for _ in range(3):
    A, B, M = map(int, input().rstrip().split())

    As = [int(x) for x in input().rstrip().split()]
    Bs = [int(x) for x in input().rstrip().split()]

    min_val = min(As) + min(Bs)

    for i in range(M):
        x, y, c = map(int, input().rstrip().split())
        val = As[x-1] + Bs[y-1] - c
        if min_val > val:
            min_val = val
    print(min_val)
    assert min_val == int(input().rstrip())
    print(input().rstrip())
