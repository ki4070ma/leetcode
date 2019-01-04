#!/usr/bin/python3

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        if x < 0:
            return False
        elif len(s) == 1:
            return True
        else:
            for i in range(len(s)/2):
                if s[i] != s[len(s)-i-1]:
                    return False
            return True
