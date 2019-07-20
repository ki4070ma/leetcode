# 57/59...
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 1:
            nums1.pop()
            nums1.extend(nums2)

        for p_nums2 in nums2:
            buffer = False
            for j, p_nums1 in enumerate(nums1):
                if j == 0 and p_nums1 == 0 and max(nums1) == 0:
                    buffer = True
                if p_nums1 >= p_nums2 or buffer:
                    nums1.insert(j, p_nums2)
                    nums1.pop()
                    #                    print(nums1)
                    break
                if p_nums1 == max(nums1) and j + 1 != len(nums1) and nums1[j + 1] == 0:
                    buffer = True
