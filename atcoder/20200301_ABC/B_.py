#!/usr/bin/python3

for _ in range(3):
    A = []
    for _ in range(3):
        A.extend([int(x) for x in input().rstrip().split()])
    N = int(input().rstrip())
    for _ in range(N):
        b = int(input().rstrip())
        for i, x in enumerate(A):
            if A[i] == b:
                A[i] = 'o'
    if A[0] == A[1] == A[2] == 'o' or \
        A[3] == A[4] == A[5] == 'o' or \
        A[6] == A[7] == A[8] == 'o' or \
        A[0] == A[3] == A[6] == 'o' or \
        A[1] == A[4] == A[7] == 'o' or \
        A[2] == A[5] == A[8] == 'o' or \
        A[0] == A[4] == A[8] == 'o' or \
        A[2] == A[4] == A[6] == 'o':
        print('Yes')
    else:
        print('No')
