#!/usr/bin/python3

from sys import stdin

for _ in range(1):
    N = int(stdin.readline().rstrip())
    As = map(int, stdin.readline().rstrip().split())

    data = {}
    for i, num_student in enumerate(As):
        data[i + 1] = num_student
    sorted_dict = sorted(data.items(), key=lambda x: x[1])
    print(' '.join(map(str, [x[0] for x in sorted_dict])))
