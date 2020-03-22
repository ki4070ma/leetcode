#!/usr/bin/python3

for _ in range(1):
    L = int(input().rstrip())
    import decimal

    decimal.getcontext().prec = 30
    L = decimal.Decimal(L)
    a = L / 3
    print(a * a * a)
