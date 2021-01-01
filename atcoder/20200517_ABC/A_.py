#!/usr/bin/python3

for _ in range(1):
    S = input().rstrip()
    S = int(list(S)[-1])
    if S in [2, 4, 5, 7, 9]:
        print("hon")
    elif S in [0, 1, 6, 8]:
        print("pon")
    elif S in [3]:
        print("bon")
