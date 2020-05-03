#!/usr/bin/python3

for _ in range(3):
    N = int(input().rstrip())
    d = {}
    As = [int(x) for x in input().rstrip().split()]
    print('-----')
    for i in range(1, N + 1):
        d[i] = 0
    for n in As:
        d[n] += 1
    for i in range(1, N + 1):
        print(d[i])