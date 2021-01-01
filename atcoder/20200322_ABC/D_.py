#!/usr/bin/python3

import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


from collections import deque

As = deque()

N = int(input().rstrip())
As.extend([int(x) for x in input().rstrip().split()])
d = {}  # count each num
for n in As:
    if n not in d.keys():
        d[n] = 1
    else:
        d[n] += 1
# print(f'd: {d}')

calc_combi_count = {}
calc_combi_count[1] = 0
total = 0

for n in d.values():
    if n > 1:
        if n not in calc_combi_count.keys():
            calc_combi_count[n] = combinations_count(n, 2)
        total += calc_combi_count[n]
        if n > 2 and n - 1 not in calc_combi_count.keys():
            calc_combi_count[n - 1] = combinations_count(n - 1, 2)

# print(total)
# print(calc_combi_count)
for num in As:
    if calc_combi_count != {1: 0}:
        ans = total - calc_combi_count[d[num]] + calc_combi_count[d[num] - 1]
    else:
        ans = 0
    print(ans)


for _ in range(4):
    from collections import deque

    As = deque()

    N = int(input().rstrip())
    As.extend([int(x) for x in input().rstrip().split()])
    d = {}  # count each num
    for n in As:
        if n not in d.keys():
            d[n] = 1
        else:
            d[n] += 1
    # print(f'd: {d}')

    calc_combi_count = {}
    calc_combi_count[1] = 0
    total = 0

    for n in d.values():
        if n > 1:
            if n not in calc_combi_count.keys():
                calc_combi_count[n] = combinations_count(n, 2)
            total += calc_combi_count[n]
            if n > 2 and n - 1 not in calc_combi_count.keys():
                calc_combi_count[n - 1] = combinations_count(n - 1, 2)

    # print(total)
    # print(calc_combi_count)
    for num in As:
        if calc_combi_count != {1: 0}:
            ans = total - calc_combi_count[d[num]] + calc_combi_count[d[num] - 1]
        else:
            ans = 0
        print(ans)

    # Old
    # ans = {}
    # for n in As:
    #     if n in ans.keys():
    #         print(ans[n])
    #         continue
    #     d[n] -= 1
    #     ret = 0
    #     for val in d.values():
    #         if val > 1:
    #             if val not in calc_combi_count.keys():
    #                 calc_combi_count[val] = combinations_count(val, 2)
    #             ret += calc_combi_count[val]
    #     ans[n] = ret
    #     print(ret)
    #     d[n] += 1
    print(input().rstrip())
