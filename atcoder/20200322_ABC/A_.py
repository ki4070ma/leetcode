#!/usr/bin/python3

import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

for _ in range(5):
    N, M = map(int, input().rstrip().split())
    ret = 0
    if N > 1:
        ret += combinations_count(N, 2)
    if M > 1:
        ret += combinations_count(M, 2)
    print(ret)
