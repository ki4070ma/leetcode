#!/usr/bin/python3

from sys import stdin

l = {'SUN': 7, 'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1}

for _ in range(7):
    S = stdin.readline().rstrip()
    print(l[S])


# Answer
# l = {'SUN': 7, 'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1}
# S = input().rstrip()
# print(l[S])
