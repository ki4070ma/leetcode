#!/usr/bin/python3

from sys import stdin

for _ in range(3):
    N = int(stdin.readline().rstrip())
    S = stdin.readline().rstrip()
    new_str = ""
    for a in list(S):
        ascii_code = ord(a) + N
        ascii_code = (ascii_code - 26) if ascii_code > 90 else ascii_code
        new_str += chr(ascii_code)
    print(new_str)

# Answer
# N = int(input().rstrip())
# S = input().rstrip()
# new_str = ''
# for a in list(S):
#     ascii_code = ord(a) + N
#     ascii_code = (ascii_code - 26) if ascii_code > 90 else ascii_code
#     new_str += chr(ascii_code)
# print(new_str)
