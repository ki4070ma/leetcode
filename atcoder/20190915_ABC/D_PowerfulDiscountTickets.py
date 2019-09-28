#!/usr/bin/python3

from sys import stdin


for _ in range(4):

    N, M = map(int, stdin.readline().rstrip().split())
    S = list(map(int, stdin.readline().rstrip().split()))
    S = [-x for x in S]
    import heapq

    heapq.heapify(S)

    for i in range(M):
        val = int(heapq.heappop(S) / 2)
        heapq.heappush(S, val)
    print(-sum(S))
