#!/usr/bin/python3

for _ in range(1):
    A, B = input().rstrip().split()
    a = sum([int(x) for x in list(A)])
    b = sum([int(x) for x in list(B)])
    print(max(a, b))
