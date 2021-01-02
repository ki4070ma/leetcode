#!/usr/bin/python3

for _ in range(2):
    a1, a2, a3, a4 = map(int, input().rstrip().split())
    print(min(a1, a2, a3, a4))
