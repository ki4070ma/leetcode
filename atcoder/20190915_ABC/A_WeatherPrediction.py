#!/usr/bin/python3

from sys import stdin

for _ in range(3):
    S = stdin.readline().rstrip()

    if S == 'Sunny':
        print('Cloudy')
    elif S == 'Cloudy':
        print('Rainy')
    else:
        print('Sunny')
