class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            k = len(nums)

        if len(nums) == k and (k == 0 or k == 1):
            return False
        elif len(nums) == k:
            d = {}
            for n in nums:
                if d.get(n, "a") == "a":
                    d[n] = 1
                else:
                    d[n] += 1
            if sum(d.values()) / len(d.values()) > 1:
                return True

        for i in range(len(nums) - k):
            d = {}
            for n in nums[i : i + k + 1]:
                if d.get(n, "a") == "a":
                    d[n] = 1
                else:
                    d[n] += 1
            #            print(d)
            if sum(d.values()) / len(d.values()) > 1:
                return True
        return False
