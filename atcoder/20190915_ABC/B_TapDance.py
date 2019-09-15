#!/usr/bin/python3

from sys import stdin

for _ in range(5):
    good_odd = ['R', 'U', 'D']  # Kisuu, Right
    good_even = ['L', 'U', 'D']  # Guusuu, Left
    is_Right_good = True
    is_Left_good = True
    S = list(stdin.readline().rstrip())
    result = False
    for i, s in enumerate(S, start=1):
        if i % 2 == 0 and is_Left_good:
            if s not in good_even:
                is_Left_good = False
        elif i % 2 == 1 and is_Right_good:
            if s not in good_odd:
                is_Right_good = False
    if is_Right_good and is_Left_good:
        print('Yes')
    else:
        print('No')
