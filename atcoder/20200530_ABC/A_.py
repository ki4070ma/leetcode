#!/usr/bin/python3

for _ in range(3):
    H1, M1, H2, M2, K = map(int, input().rstrip().split())
    minutes = M2 - M1
    hours = 0
    if minutes < 0:
        minutes += 60
        hours -= 1
    hours += H2 - H1
    minutes += hours * 60
    answer = minutes - K
    if answer < 0:
        answer = 0
    print(answer)
