#!/usr/bin/python3

for _ in range(1):
    S = input().rstrip()
    T = input().rstrip()
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)
