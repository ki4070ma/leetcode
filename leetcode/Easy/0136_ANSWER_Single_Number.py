class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            ret ^= num
        return ret

        return 2 * sum(list(set(nums))) - sum(nums)
