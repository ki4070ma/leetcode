#!/usr/bin/python3

from sys import stdin

# 1 -> 1 attack
# 2 -> 3
# 3 -> 3
# 4 -> 7
# 5

for _ in range(8):
    H = int(input().rstrip())
    ret = 0
    if H == 1:
        ret = 1
    elif H in [2, 3]:
        ret = 3
    else:
        count = 0
        while H != 1:
            H = H // 2
            count += 1
        ret = 3
        print(count)
        for i in range(count - 1):
            ret = 2 * ret + 1
    print(ret)

# def calc(target_monster_hitpoint, monster_list, dict_calc, cost):
#     if target_monster_hitpoint == 1:
#         cost += 1
#         return monster_list, dict_calc, cost
#     else:
#         if target_monster_hitpoint in dict_calc.keys():
#             pass
#
#
# for _ in range(8):
#     H = int(input().rstrip())
#     l = [H]
#     d = {}
#     ret = 0
#     while len(l) > 0:
#         hit_point = l.pop()
#         if hit_point in d.keys():
#             ret += d[hit_point]
#         else:
#             if hit_point == 1:
#                 ret += 1
#             else:
#                 tmp = hit_point // 2
#                 l.extend([tmp, tmp])
