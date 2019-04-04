class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        import sys
        max_val = -sys.maxsize
        ret = []
        for length in range(1, len(nums)+1):
            for pos in range(len(nums)-length+1):
                val = sum(nums[pos:pos+length])
                if val > max_val:
                    max_val = val
#                    ret = nums[pos:pos+length]
#                    print(ret)
#                print(nums[pos:pos+length])
        return max_val
