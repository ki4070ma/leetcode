#!/usr/bin/python3

for _ in range(10):
    H, W = map(int, input().rstrip().split())
    D = []
    for h in range(H):
        D.append(list(input().rstrip()))
    # print(*D, sep='\n')
    d = {}
    for i in range(1, H + W):  # i: total
        for h in range(i):
            if h > H - 1:
                h = H - 1
            w = i - h - 1
            if w > W - 1 or h > H - 1 or w < 0 or h < 0:
                continue
            # print(h, w)
            if (h - 1, w) in d.keys() and (h, w - 1) in d.keys():
                d[(h, w)] = min(d[(h - 1, w)], d[(h, w - 1)])
            elif (h - 1, w) in d.keys():
                d[(h, w)] = d[(h - 1, w)]
            elif (h, w - 1) in d.keys():
                d[(h, w)] = d[(h, w - 1)]
            else:
                d[(h, w)] = 0
            if D[h][w] == "#":
                d[(h, w)] += 1
    print(d[(H - 1, W - 1)])
    assert d[(H - 1, W - 1)] == int(input().rstrip())
    print(input().rstrip())
