#!/usr/bin/python3

from sys import stdin

for _ in range(7):
    abc = "ABC"
    N = int(stdin.readline().rstrip())
    S = stdin.readline().rstrip()
    #    print('N: {}, S: {}'.format(N, S))
    ret = 0
    if N == 3 and S == abc:
        ret = 1
    else:
        for i in range(N - len(abc) + 1):
            if abc == S[i : i + 3]:
                ret += 1
    print(ret)
