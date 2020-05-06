#!/usr/bin/python3

for _ in range(3):
    S, W = map(int, input().rstrip().split())
    if S <= W:
        print('unsafe')
    else:
        print('safe')
