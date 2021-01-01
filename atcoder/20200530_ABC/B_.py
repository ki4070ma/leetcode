#!/usr/bin/python3


for _ in range(1):
    from collections import deque

    T = input().rstrip()
    d = deque()
    d.extend(list(T))
    answer = deque()
    window = deque(maxlen=3)
    for a in d:
        if a == "?":
            answer.append("D")
        else:
            answer.append(a)
    print("".join(answer))
