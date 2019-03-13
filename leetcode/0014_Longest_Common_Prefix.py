#!/usr/bin/python3

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Brute force
        if not strs:
            return ''
        min_word = strs[0]
        minlength = len(strs[0])
        for x in range(len(strs)):
            if minlength > len(strs[x]):
                minlength = len(strs[x])
                min_word = strs[x]
        for w in range(minlength, 0, -1):
            for l in range(len(min_word) - w + 1):
                s = min_word[l:l+w]
                chk = [x for x in strs if x.startswith(s)]
                if len(chk) == len(strs):
                    return s
        return ''
