#!/usr/bin/python3


def search_touched_idx(i, val, l):
    ret = []
    base_idx = val[0]
    arm_length = val[1]
    if arm_length != 0:
        minus_idx = base_idx - arm_length
        plus_idx = base_idx + arm_length
        for n in range(i - 1, 0, -1):
            if minus_idx < l[n][0]:
                ret.append(n)
            else:
                break

        for n in range(i + 1, len(l)):
            if l[n][0] < plus_idx:
                ret.append(n)
            else:
                break
    return ret


for _ in range(3):
    N = int(input().rstrip())
    l = []
    for i in range(N):
        l.append(list(map(int, input().rstrip().split())))
    # print(l)

    touch = []  # stored touched idx to list
    l.sort(key=lambda x: x[0])
    count = 0
    prev_robot_touched = False
    for i, val in enumerate(l):
        # touch.append(search_touched_idx(i, val, l))
        tmp = len(search_touched_idx(i, val, l))
        if tmp and not prev_robot_touched:
            prev_robot_touched = True
            count += 1
        else:
            prev_robot_touched = False
    # print(touch)
    print(len(l) - count)
