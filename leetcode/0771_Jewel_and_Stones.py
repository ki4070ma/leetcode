class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # 1 liner
        return sum([S.count(jewel) for jewel in list(J)])

        # basic
        count = 0
        for jewel in list(J):
            count += S.count(jewel)
        return count
