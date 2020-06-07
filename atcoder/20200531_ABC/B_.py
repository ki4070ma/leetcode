#!/usr/bin/python3

for _ in range(3):
    N = input().rstrip()
    As = [int(x) for x in input().rstrip().split()]
    ret = 1
    if 0 in As:
        ret = 0
    else:
        for x in As:
            ret *= x
            if ret > 10 ** 18:
                ret = -1
                break
    print(ret)
