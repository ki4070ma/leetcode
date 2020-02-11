#!/usr/bin/python3


for _ in range(9):

    N, K = map(int, input().rstrip().split())
    Ps = [int(x) for x in input().rstrip().split()]

    Ps_sum_list = []
    Ps_sum = 0
    for x in Ps:
        Ps_sum += x
        Ps_sum_list.append(Ps_sum)

    max_val = 0
    if K == 1:
        max_val = max(Ps)
        print((max_val + 1) / 2)
    elif N == K:
        max_val = Ps_sum_list[-1]
        print((max_val + K) / 2)
    else:
        for i in range(N - K):
            val = Ps_sum_list[i + K] - Ps_sum_list[i]
            if val > max_val:
                max_val = val
        print((max_val + K) / 2)

    # base_i = 0
    # max_val = 0
    # for i in range(len(Ps) - K + 1):
    #     sum_val = sum(Ps[i:i + K])
    #     if max_val < sum_val:
    #         max_val = sum_val
    #         base_i = i
    # print((sum(Ps[base_i:base_i + K]) + K) / 2)
