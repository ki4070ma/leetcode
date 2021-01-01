#!/usr/bin/python3

for _ in range(4):
    N, T = map(int, input().rstrip().split())
    shops = []
    for _ in range(N):
        a, b = map(int, input().rstrip().split())
        shops.append([a, b])

    max_shop_num = 0
    t = 0
    import sys

    # 2. Idea: WA
    while t < T + 0.5:
        min_t = sys.maxsize
        idx = 0
        for i in range(len(shops)):
            a, b = shops[i]
            if (t + 1) * a + b < min_t:
                min_t = (t + 1) * a + b
                idx = i
        t += 1 + min_t
        if t <= T + 0.5:
            max_shop_num += 1
        if len(shops) == 0:
            break
        else:
            shops = shops[:idx] + shops[idx + 1 :]

    print(max_shop_num)

    # # 1. Brute force (TLE)
    # import itertools
    # max_shop_num = 0
    # # print(list(itertools.permutations(list(range(N)))))
    # for route in itertools.permutations(list(range(N))):
    #     shop_num = 0
    #     t = 0
    #     for i in list(route):
    #         t += 1
    #         a, b = shops[i]
    #         tmp_t = t + a * t + b
    #         if tmp_t > T + 0.5:
    #             if max_shop_num < shop_num:
    #                 max_shop_num = shop_num
    #             break
    #         else:
    #             t = tmp_t
    #             shop_num += 1
    #     else:
    #         if max_shop_num < shop_num:
    #             max_shop_num = shop_num

    assert max_shop_num == int(input().rstrip())
    print(input())
