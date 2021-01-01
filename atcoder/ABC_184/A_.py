#!/usr/bin/python3

for _ in range(3):
    a, b = map(int, input().rstrip().split())
    c, d = map(int, input().rstrip().split())
    print(a * d - b * c)
