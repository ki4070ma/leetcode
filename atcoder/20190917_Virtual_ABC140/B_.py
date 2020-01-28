#!/usr/bin/python3

for _ in range(2):
    N = int(input().rstrip())
    Idxs = [int(x) for x in input().rstrip().split()]
    Bs = [int(x) for x in input().rstrip().split()]
    Cs = [int(x) for x in input().rstrip().split()]

    ret = 0
    prev = -100
    for idx in Idxs:
        ret += Bs[idx - 1]
        if idx - 1 == prev:
            ret += Cs[prev - 1]
        prev = idx
    print(ret)
