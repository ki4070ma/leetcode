#!/usr/bin/python3

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        elif needle not in haystack:
            return -1
        return len(haystack.split(needle)[0])
