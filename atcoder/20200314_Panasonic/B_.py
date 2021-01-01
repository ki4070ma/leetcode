#!/usr/bin/python3

for _ in range(5):
    H, W = map(int, input().rstrip().split())
    tmp = H * W
    if H == 1 or W == 1:
        print(1)
    elif tmp % 2 == 0:
        print(int(tmp / 2))
    else:
        print(int((tmp - 1) / 2 + 1))
