#!/usr/bin/python3

for _ in range(3):
    A = []
    for _ in range(3):
        A.extend([int(x) for x in input().rstrip().split()])
    N = int(input().rstrip())
    for i in range(N):
        tmp = int(input().rstrip())
        for j, x in enumerate(A):
            if A[j] == tmp:
                A[j] = 'o'
    if A[0] == 'o' and A[1] == 'o' and A[2] == 'o':
        print('Yes')
    elif A[3] == 'o' and A[4] == 'o' and A[5] == 'o':
        print('Yes')
    elif A[6] == 'o' and A[7] == 'o' and A[8] == 'o':
        print('Yes')
    elif A[0] == 'o' and A[3] == 'o' and A[6] == 'o':
        print('Yes')
    elif A[1] == 'o' and A[4] == 'o' and A[7] == 'o':
        print('Yes')
    elif A[2] == 'o' and A[5] == 'o' and A[8] == 'o':
        print('Yes')
    elif A[0] == 'o' and A[4] == 'o' and A[8] == 'o':
        print('Yes')
    elif A[2] == 'o' and A[4] == 'o' and A[6] == 'o':
        print('Yes')
    else:
        print('No')
