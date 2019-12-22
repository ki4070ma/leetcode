#!/usr/bin/python3

from sys import stdin

for _ in range(3):
    N = int(stdin.readline().rstrip())
    As = [int(x) for x in stdin.readline().rstrip().split()]

    base = 1
    l = []
    for x in As:
        if x == base:
            l.append(x)
            base += 1

    if len(l) == 0:
        print('-1')
    else:
        print(N - len(l))
