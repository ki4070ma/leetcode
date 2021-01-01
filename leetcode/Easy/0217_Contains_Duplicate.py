class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        d = {}
        for num in nums:
            if d.get(num, "a") == "a":
                d[num] = 1
            else:
                d[num] += 1
        if sum(d.values()) / len(d.values()) > 1:
            return True
        return False
