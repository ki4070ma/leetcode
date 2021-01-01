#!/usr/bin/python3


def chk_fizzbuzz(i):
    if i % 3 == 0 or i % 5 == 0 or i % 15 == 0:
        return 0
    else:
        return i


for _ in range(2):
    N = int(input().rstrip())
    ret = 0
    for i in range(N + 1):
        ret += chk_fizzbuzz(i)
    print(ret)
