#!/usr/bin/python3

for _ in range(3):
    N, X = map(int, input().rstrip().split())
    S = input().rstrip()
    for x in list(S):
        if x == 'o':
            X += 1
        elif x == 'x' and X > 0:
            X -= 1
    print(X)
