#!/usr/bin/python3

for _ in range(3):
    S = input().rstrip()
    N = len(S)
    if (
        S == S[::-1]
        and S[: int((N - 1) / 2)] == S[: int((N - 1) / 2)][::-1]
        and S[int((N + 3) / 2) - 1 : N] == S[int((N + 3) / 2) - 1 : N][::-1]
    ):
        print("Yes")
    else:
        print("No")
