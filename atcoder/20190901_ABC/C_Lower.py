#!/usr/bin/python3

from sys import stdin

for _ in range(3):
    N = int(stdin.readline().rstrip())
    Hs = list(map(int, stdin.readline().rstrip().split()))

    # print(Hs)

    count = 0
    ret_count = 0
    prev_val = Hs[-1]

    for H in Hs[:-1][::-1]:
        # print('prev_val: ' + str(prev_val))
        # print('H: ' + str(H))
        # print('ret_count: ' + str(ret_count))
        if prev_val <= H:
            count += 1
        else:
            if ret_count < count:
                ret_count = count
            count = 0
        prev_val = H

    if ret_count < count:
        ret_count = count

    print(ret_count)
