#!/bin/python3

import math
import os
import random
import re
import sys

# TODO Didn't consider about less swap case. 入れ替えたときに一気に並び替えが解消されるケースが考慮されていない.

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    length = len(arr)
    target_list = range(1, length + 1)
    diff = 0
    for a, b in zip(arr, target_list):
        if a != b:
            diff += 1
    duplicate = 0
    for i, c in enumerate(arr):
        if arr[c - 1] == i + 1 and c != arr[c - 1]:
            print("****")
            print(c)
            print(arr[c - 1])
            duplicate += 1
    diff = diff - int(duplicate / 2)
    return diff - 1


if __name__ == "__main__":
    #    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #    n = int(input())

    #    arr = list(map(int, input().rstrip().split()))
    input_str = "8 45 35 84 79 12 74 92 81 82 61 32 36 1 65 44 89 40 28 20 97 90 22 87 48 26 56 18 49 71 23 34 59 54 14 16 19 76 83 95 31 30 69 7 9 60 66 25 52 5 37 27 63 80 24 42 3 50 6 11 64 10 96 47 38 57 2 88 100 4 78 85 21 29 75 94 43 77 33 86 98 68 73 72 13 91 70 41 17 15 67 93 62 39 53 51 55 58 99 46"
    arr = list(map(int, input_str.rstrip().split()))

    res = minimumSwaps(arr)

#    fptr.write(str(res) + '\n')

#    fptr.close()
