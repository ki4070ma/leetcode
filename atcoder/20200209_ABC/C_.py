#!/usr/bin/python3

for _ in range(3):
    N = int(input().rstrip())
    As = [int(x) for x in input().rstrip().split()]

    d = {}
    for x in As:
        if x not in d.keys():
            d[x] = 1
        else:
            d[x] += 1
    if len(As) == len(d):
        print("YES")
    else:
        print("NO")
