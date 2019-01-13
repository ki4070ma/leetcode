#!/usr/bin/python3

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Brute force
        if len(nums) < 2:
            return []
        ret = []
        ret_set = []
        nums = sorted(nums)
        for l in range(len(nums) - 2):
            for c in range(l+1, len(nums) - 1):
                val = -(nums[l] + nums[c])
                if val in nums[c+1:] and set([nums[l], nums[c], val]) not in ret_set:
                    ret.append([nums[l], nums[c], val])
                    ret_set.append(set([nums[l], nums[c], val]))
        return ret
