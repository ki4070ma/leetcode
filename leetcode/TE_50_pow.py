class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = float(1/x)
            n = -n
        elif n == 0:
            return 1
        ret = 1
        for _ in range(n):
            ret *= x
        return ret
