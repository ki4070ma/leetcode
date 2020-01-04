class Solution:
    def climbStairs(self, n: int) -> int:
        count_1 = n
        count_2 = 0
        ret = 0
        while (count_1 >= 0):
#            print(count_1)
            ret += self.combinations_count(count_1 + count_2, count_1)
            count_1 -= 2
            count_2 += 1
        return ret


    def combinations_count(self, n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

