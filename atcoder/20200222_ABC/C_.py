#!/usr/bin/python3

for _ in range(2):
    N = int(input().rstrip())
    Xs = [int(x) for x in map(int, input().rstrip().split())]
    import sys

    sum_val = sys.maxsize
    for i in range(min(Xs), max(Xs) + 1):
        tmp_sum_val = 0
        for j in Xs:
            tmp_sum_val += (j - i) ** 2
        if sum_val > tmp_sum_val:
            sum_val = tmp_sum_val
    print(sum_val)
