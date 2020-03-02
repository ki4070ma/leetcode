#!/usr/bin/python3

for _ in range(3):
    N = int(input().rstrip())
    if N % 2 == 0:
        print(int(N / 2))
    else:
        print(int(N // 2 + 1))
