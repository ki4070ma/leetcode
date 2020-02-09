#!/usr/bin/python3


for _ in range(3):
    from collections import deque

    N, K = map(int, input().rstrip().split())
    Ps = [int(x) for x in input().rstrip().split()]

    if K == 1:
        print((max(Ps) + 1) / 2)
    else:
        max_val = 0
        d = deque(maxlen=K)
        for i, n in enumerate(Ps):
            if i < K:
                d.append(n)
                continue
            popleft_val = d.popleft()
            d.append(n)
            if popleft_val >= n:
                continue
            val = sum(d)
            if max_val < val:
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
