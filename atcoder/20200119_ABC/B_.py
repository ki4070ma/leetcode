#!/usr/bin/python3

for _ in range(2):
    a, b = map(int, input().rstrip().split())
    str1 = str(a) * b
    str2 = str(b) * a
    ret = str1 if str1 < str2 else str2
    print(ret)
