#!/usr/bin/python3

for _ in range(3):
    N = int(input().rstrip())
    As = {}
    answer = 0
    for a in [int(x) for x in input().rstrip().split()]:
        answer += a
        if a in As.keys():
            As[a] += 1
        else:
            As[a] = 1
    # print(As)
    Q = int(input().rstrip())
    d = {}
    for i in range(Q):
        b, c = map(int, input().rstrip().split())
        d[i] = {'b': b, 'c': c}
    # print(d)
    for i in sorted(d.keys()):
        if d[i]['b'] in As.keys():
            diff = d[i]['c'] - d[i]['b']
            diff_num = As.pop(d[i]['b'])
            if d[i]['c'] in As.keys():
                As[d[i]['c']] += diff_num
            else:
                As[d[i]['c']] = diff_num
            answer += (diff * diff_num)
        print(answer)
    print('---')


