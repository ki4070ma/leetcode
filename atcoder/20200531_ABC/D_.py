#!/usr/bin/python3


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def calc(n):
    ret = 0
    for i in range(1, 1000):
        n -= i
        if n == 0:
            ret = i
            break
        elif n < 0:
            ret = i - 1
            break
    return ret


for _ in range(5):
    N = int(input().rstrip())
    d = {}
    for x in prime_factorize(N):
        if x not in d.keys():
            d[x] = 1
        else:
            d[x] += 1
    ret = 0
    for x in d.values():
        ret += calc(x)
    print(ret)
