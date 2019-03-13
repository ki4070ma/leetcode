#!/usr/bin/python3

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        ret = s[0]
        for center in range(len(s)):
            # Odd
            for l in range(min([center, len(s) - 1 - center]) + 1):
                if s[center - l] == s[center + l]:
                    tmp = s[center - l:center + l + 1]
                    if len(ret) < len(tmp):
                        ret = tmp
                else:
                    break
            # Even
            for l in range(min([center + 1, len(s) - (center + 1)])):
                if s[center - l] == s[center + l + 1]:
                    tmp = s[center - l:(center + l + 1) + 1]
                    if len(ret) < len(tmp):
                        ret = tmp
                else:
                    break
        return ret

        # Brute force
        if len(s) < 2:
            return s
        ret = s[0]
        for i in range(len(s)):
            for j in range(i + 2, len(s) + 1):
                sub_s = s[i:j]
                length = len(sub_s)
                if len(ret) > length:
                    continue
                palindrome = True
                for k in range(length / 2):
                    if sub_s[k] != sub_s[-1 - k]:
                        palindrome = False
                        break
                if palindrome and len(ret) < len(sub_s):
                    ret = sub_s
        return ret
