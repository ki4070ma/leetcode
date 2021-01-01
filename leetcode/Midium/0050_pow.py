class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Others' answer: https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)

        # Brute force
        if n < 0:
            x = float(1 / x)
            n = -n
        elif n == 0:
            return 1
        ret = 1
        for _ in range(n):
            ret *= x
        return ret
