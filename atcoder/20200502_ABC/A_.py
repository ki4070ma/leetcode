#!/usr/bin/python3

for _ in range(6):
    K = int(input().rstrip())
    A, B = map(int, input().rstrip().split())

    ok_flg = False
    for i in range(A, B + 1):
        if i % K == 0:
            print('OK')
            ok_flg = True
            break
    if not ok_flg:
        print('NG')

    # amari = A % K
    # if K == 1:
    #     print('OK')
    # elif K == A or K == B:
    #     print('OK')
    # elif (A - amari) + K <= B:
    #     print('OK')
    # else:
    #     print('NG')

