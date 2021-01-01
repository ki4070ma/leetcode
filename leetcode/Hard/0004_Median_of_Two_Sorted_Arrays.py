#!/usr/bin/python3


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = sorted(nums1 + nums2)
        length = len(l)
        if len(l) % 2 == 1:
            return l[length / 2]
        else:
            return (l[length / 2 - 1] + l[length / 2]) / 2.0
