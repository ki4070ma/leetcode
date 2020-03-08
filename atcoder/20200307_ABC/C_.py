#!/usr/bin/python3

for _ in range(4):
    A, B = map(int, input().rstrip().split())
    ret = 1000000
    for i in range(1, 10001):
        if int(i * 0.08) == A and int(i * 0.1) == B and ret > i:
            ret = i
            break
    if ret == 1000000:
        ret = -1
    print(ret)
    assert ret == int(input().rstrip())

