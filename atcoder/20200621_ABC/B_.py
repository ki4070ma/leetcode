#!/usr/bin/python3

for _ in range(1):
    N, K = map(int, input().rstrip().split())
    pn = [int(x) for x in input().rstrip().split()]
    print(sum(sorted(pn)[:K]))

