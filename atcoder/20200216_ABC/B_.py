#!/usr/bin/python3

for _ in range(2):
    N = int(input().rstrip())
    As = [int(x) for x in input().rstrip().split()]
    fail_flg = False
    for a in As:
        if a % 2 == 1:
            continue
        elif not (a % 2 == 0 and (a % 3 == 0 or a % 5 == 0)):
            fail_flg = True
            break
    if fail_flg:
        print('DENIED')
    else:
        print('APPROVED')

