#!/usr/bin/python3

from sys import stdin

def calc(N):
    return A * N + B * len(str(N))

for _ in range(4):
    A, B, X = map(int, stdin.readline().rstrip().split())
    # print(A)
    # print(B)
    # print(X)
    # "A x N + B x d(N)"
    max_N = 10**9
    max_price = calc(max_N)
    if X > max_price:
        print(max_N)
    else:
        # ONGOING
        # count = 1
        # pivot = int(max_N / 2**count)
        # while True:
        #     val = calc(pivot)
        #     if X < val:
        #         pivot -= int(max_N / 2**(count+1))
        #     elif X > val:
        #         pivot += int(max_N / 2**(count+1))
        #     else:
        #         print(pivot)
        #         break
        #     count += 1
        prev_N = 0
        for N in range(max_N):
            price = A * N + B * len(str(N))
            if price > X:
                # print('price: {}'.format(price))
                prev_N = N - 1
                break
        if prev_N < 0:
            prev_N = 0
        print(prev_N)
