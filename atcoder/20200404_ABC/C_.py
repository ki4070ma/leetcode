#!/usr/bin/python3

for _ in range(3):
    N, K = map(int, input().rstrip().split())
    amari = N % K
    amari_2 = abs(amari - K)
    print(min(amari, amari_2))
