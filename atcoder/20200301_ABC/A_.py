#!/usr/bin/python3

for _ in range(3):
    N = int(input().rstrip())

    # Answer1
    # print(N//2 + N % 2)

    # Answer2
    import math
    print(math.ceil(N/2))

    # Answer3
    # if N % 2 == 0:
    #     print(int(N // 2))
    # else:
    #     print(int(N // 2 + 1))
