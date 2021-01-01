#!/usr/bin/python3

for _ in range(7):
    # ord('a'), chr(97)
    N = int(input().rstrip())
    ret = []
    while N != 0:
        char = chr(96 + (N % 26))
        if char == "`":
            char = "z"
            N = N // 26 - 1
        else:
            N = N // 26
        ret.append(char)
    print("".join(ret[::-1]))
