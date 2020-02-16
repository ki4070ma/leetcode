#!/usr/bin/python3

for _ in range(5):
    N = int(input().rstrip())
    d = {}
    for _ in range(N):
        string = input().rstrip()
        if string in d.keys():
            d[string] += 1
        else:
            d[string] = 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    # print(d)
    rets = []
    max = -1
    for string, val in d:
        if max == -1:
            max = val
        elif max != val:
            break
        rets.append(string)

    for a in sorted(rets):
        print(a)

    print('---')
