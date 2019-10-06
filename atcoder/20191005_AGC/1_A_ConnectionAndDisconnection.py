#!/usr/bin/python3

from sys import stdin

for _ in range(13):
    S = stdin.readline().rstrip()
    K = int(stdin.readline().rstrip())

    pre_str = ''
    count = 1
    base_count = 0
    for a in list(S):
        if pre_str == a:
            count += 1
        else:
            base_count += int(count / 2)
            count = 1
            pre_str = a
    base_count += int(count / 2)
    ret = 0
    if not S:
        ret = 0
    if len(list(set(list(S)))) == 1:
        ret = int(len(S) * K / 2)
    elif len(S) > 2 and S[0] != S[1] and S[-1] != S[-2] and S[0] == S[-1]:
        ret = base_count * K
        ret += K - 1
    else:
        ret = base_count * K
    print(ret)

# for _ in range(3):
#     S = stdin.readline().rstrip()
#     K = int(stdin.readline().rstrip())
#
#     string = S*K
#     print(string)
#
#     pre_str = ''
#     count = 1
#     ret = 0
#     for a in list(string):
#         if pre_str == a:
#             count += 1
#         else:
#             ret += int(count / 2)
#             count = 1
#             pre_str = a
#     ret += int(count / 2)
#     print(ret)
