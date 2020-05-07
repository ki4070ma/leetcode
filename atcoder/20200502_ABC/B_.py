#!/usr/bin/python3

for _ in range(3):
    X = int(input().rstrip())
    val = 100
    count = 0
    while True:
        val = int(1.01 * val)
        count += 1
        if val >= X:
            break
    print(count)