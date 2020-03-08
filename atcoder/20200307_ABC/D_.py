#!/usr/bin/python3

for _ in range(3):
    S = input().rstrip()
    Q = int(input().rstrip())
    reversed = False
    for _ in range(Q):
        l = input().rstrip()
        if l.startswith('1'):
            reversed = False if reversed else True
        else:
            _, F, C = l.split()
            if F == '1':
                if reversed:
                    S = S + C
                else:
                    S = C + S
            else:
                if reversed:
                    S = C + S
                else:
                    S = S + C
    if reversed:
        ret = S[::-1]
    else:
        ret = S
    print(ret)
    assert ret == input().rstrip()
    print(input().rstrip())
