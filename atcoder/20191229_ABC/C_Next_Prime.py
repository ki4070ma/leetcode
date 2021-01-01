#!/usr/bin/python3

from sys import stdin


def is_prime_editorial(num):
    if num <= 1:
        return False
    i = 2
    while i * i < num:
        if num % i == 0:
            return False
        i += 1
    return True


def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    from math import sqrt

    sqrtnum = sqrt(num)
    i = 3
    while i <= sqrtnum:
        if num % i == 0:
            return False
        i += 2
    return True


for _ in range(3):
    X = int(stdin.readline().rstrip())

    while True:
        if is_prime(X):
            print(X)
            break
        X += 1
