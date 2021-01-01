#!/usr/bin/python3


def show(ret):
    print(" ".join([str(x) for x in ret]))


for _ in range(3):
    N, K = map(int, input().rstrip().split())
    As = [int(x) for x in input().rstrip().split()]
    show(As)
    ret = []
    for x in range(K):
        ret = []
        for y in range(len(As)):
            add = 0
            for z in range(len(As)):
                if abs(y - z) <= As[z]:
                    add += 1
            ret.append(add)
        As = ret[:]
        show(ret)
    show(ret)
    print("----")
