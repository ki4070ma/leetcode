#!/usr/bin/python3

from sys import stdin

for _ in range(1):
    N, M = map(int, stdin.readline().rstrip().split())
    # print('N: {}, M: {}'.format(N, M))
    AC = 0
    WA = 0
    # {'Q num': {'AC': bool, 'WA': int}}
    data = {}
    for _ in range(M):
        tmp = stdin.readline().rstrip().split()
        p, S =  int(tmp[0]), tmp[1]
        print(data)
        print('p: {}, S: {}'.format(p, S))
        print('{} {}'.format(AC, WA))
        if p not in data.keys():
            if S == 'AC':
                data[p] = {'AC': True, 'WA': 0}
                AC += 1
            elif S == 'WA':
                print('***HOGE')
                data[p] = {'AC': False, 'WA': 1}
        elif p in data.keys():
            if S == 'AC':
                if data[p]['AC'] is True:
                    continue
                elif data[p]['AC'] is False:
                    data[p]['AC'] = True
                    WA += data[p]['WA']
                    AC += 1
            elif S == 'WA':
                if data[p]['AC'] is True:
                    continue
                elif data[p]['AC'] is False:
                    data[p]['WA'] = data[p]['WA'] + 1
    print('{} {}'.format(AC, WA))
