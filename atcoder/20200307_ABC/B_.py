#!/usr/bin/python3

for _ in range(10):
    N, A, B = map(int, input().rstrip().split())
    if A == 0:
        ret = 0
    elif A + B == 0:
        ret = 0
    else:
        ret = int(N / (A + B)) * A + N % (A + B) if A > N % (A + B) else A
    print(ret)
    assert int(input().rstrip()) == ret
