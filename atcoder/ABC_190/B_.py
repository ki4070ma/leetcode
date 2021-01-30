#!/usr/bin/python3

for _ in range(3):
    N, S, D = map(int, input().rstrip().split())
    ret = 'No'
    for _ in range(N):  
        X, Y = map(int, input().rstrip().split())
        if S > X and D < Y and ret == 'No':
            ret = 'Yes'
    print(ret)
