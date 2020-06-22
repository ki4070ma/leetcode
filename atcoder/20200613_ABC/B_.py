#!/usr/bin/python3

for _ in range(3):
    A, V = map(int, input().rstrip().split())
    B, W = map(int, input().rstrip().split())
    T = int(input().rstrip())
    d = abs(A - B)
    v = V - W
    if v <= 0:
        print('NO')
    elif d % v != 0:
        print('NO')
    elif T < d / v:
        print('NO')
    else:
        print('YES')
