#!/usr/bin/python3


for _ in range(9):
    import math

    a, b, H, M = map(int, input().rstrip().split())
    if H == 0 and M == 0:
        print(abs(a - b))
    else:
        H = H * 5 + (float(M) / 12)
        kakudo = abs(H - M)
        kakudo *= 6
        print(
            math.sqrt(
                float(a * a) + float(b * b) - 2 * a * b * math.cos(math.radians(kakudo))
            )
        )
