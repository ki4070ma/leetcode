#!/usr/bin/python3

from sys import stdin

for _ in range(2):
    A, B = map(int, stdin.readline().rstrip().split())

    As = []
    Bs = []

    ret = []
    for i in range(2, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            ret.append(i)

    print(ret[::-1])

    result = []
    for i, a in enumerate(ret):
        data = []
        for b in ret[i + 1 :]:
            tmp = "T" if b % a == 0 else "F"
            data.append(tmp)
        if data:
            print([a] + data[::-1])
