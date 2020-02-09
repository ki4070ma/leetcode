#!/usr/bin/python3

for _ in range(2):
    S, T = input().rstrip().split()
    A, B = map(int, input().rstrip().split())
    U = input().rstrip()

    d = {S: A, T: B}
    d[U] -= 1
    print('{} {}'.format(d[S], d[T]))
