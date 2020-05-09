#!/usr/bin/python3

def calc(x):
    return int(A*x/B) - A*int(x/B)

for _ in range(4):
    A, B, N = map(int, input().rstrip().split())
    print(calc(min(B - 1, N)))
    if N < 10000:
        val = -1
        for x in range(N):
            tmp = calc(x)
            # print(tmp)
            if val < tmp:
                val = tmp
        # print(val)
    else:
        p = int(N/2)
        l = [calc(x) for x in range(p-2, p+2)]
        print(l)

    print(calc(min(B-1, N)))
