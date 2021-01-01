class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d[n] + 1 if n in d.keys() else 1
        val, ret = 0, 0
        for key in d.keys():
            if val < d[key]:
                ret, val = key, d[key]
        return ret
