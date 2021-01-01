#!/usr/bin/python3

for _ in range(4):
    l = [int(x) for x in input().rstrip().split()]
    d = {}
    for x in l:
        if x in d.keys():
            d[x] += 1
        else:
            d[x] = 1
    if 2 in d.values():
        print("Yes")
    else:
        print("No")
