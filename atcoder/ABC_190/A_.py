#!/usr/bin/python3

for _ in range(3):
    A, B, C = map(int, input().rstrip().split())
#    print(A, B, C)
    if A > B:
        print('Takahashi')
    elif A < B:
        print('Aoki')
    elif A == B:
        if C == 0:
            print('Aoki')
        elif C == 1:
            print('Takahashi')
