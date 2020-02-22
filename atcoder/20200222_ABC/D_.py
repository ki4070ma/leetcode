#!/usr/bin/python3

import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

for _ in range(2):
    n, a, b = map(int, input().rstrip().split())
    print(n, a, b)
    l = {}
    ret = 0
    print(combinations_count(n, a))
    print(combinations_count(n, b))
    print(2**n)
    print('A')
    hiku = combinations_count(n, a)
    print('B')
    hiku += combinations_count(n, b)
    print('C')
    print((2**n - hiku - 1) % (10**9+7))
    # for i in range(n):
    #     if i in [a, b]:
    #         continue
    #     if n - i in l.keys():
    #         ret += l[n-i]
    #     else:
    #         ret += combinations_count(n, i)
    #         l[i] = n
    # print(ret % (10**9+7))
