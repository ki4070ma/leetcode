#!/usr/bin/python3

for _ in range(5):
    a, b, c = map(int, input().rstrip().split())
    from decimal import *

    getcontext().prec = 500  # NG: 1000
    if (Decimal(a).sqrt() + Decimal(b).sqrt()) < Decimal(c).sqrt():
        print("Yes")
    else:
        print("No")
