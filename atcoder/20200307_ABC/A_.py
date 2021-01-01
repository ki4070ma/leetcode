#!/usr/bin/python3

for _ in range(4):
    S = input().rstrip()
    if len(set(list(S))) == 1:
        print("No")
    else:
        print("Yes")
