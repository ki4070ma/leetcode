#!/usr/bin/python3

for _ in range(3):
    S = input().rstrip()
    Q = int(input().rstrip())
    reversed = False
    from collections import deque

    q = deque()
    q.extend(list(S))
    for _ in range(Q):
        l = input().rstrip()
        if l.startswith("1"):
            reversed = False if reversed else True
        else:
            _, F, C = l.split()
            if F == "1":
                if reversed:
                    q.append(C)
                else:
                    q.appendleft(C)
            elif F == "2":
                if reversed:
                    q.appendleft(C)
                else:
                    q.append(C)
    ret = "".join(list(q)[::-1]) if reversed else "".join(list(q))
    print(ret)
    assert ret == input().rstrip()
    print(input().rstrip())
