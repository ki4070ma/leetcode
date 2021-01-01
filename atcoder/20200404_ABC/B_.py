#!/usr/bin/python3

for _ in range(3):
    N, M = map(int, input().rstrip().split())
    As = [int(x) for x in input().rstrip().split()]
    # print(N, M)
    # print(As)
    total = sum(As)
    count = len([True for x in As if x >= total / (4 * M)])
    if count >= M:
        print("Yes")
    else:
        print("No")
