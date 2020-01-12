#!/usr/bin/python3

from sys import stdin

for _ in range(2):
    print(chr(ord(stdin.readline().rstrip()) + 1))
