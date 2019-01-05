#!/usr/bin/python3

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Two pointer approach
        if len(height) < 1:
            return 0
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            h_l = height[l]
            h_r = height[r]
            h = min(h_l, h_r)
            val = h * (r - l)
            if val > area:
                area = val
            if h_l > h_r:
                r -= 1
            else:
                l += 1
        return area

        # Brute force
        sq = 0
        max_h = max(height)
        for a in range(len(height) - 1):
            for b in range(len(height) - 1, a, -1):
                h = min(height[a], height[b])
                if sq > max_h * (b - a):
                    break
                val = h * (b - a)
#                print(val)
                if sq < val:
                    sq = val
        return sq
