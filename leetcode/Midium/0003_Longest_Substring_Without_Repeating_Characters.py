#!/usr/bin/python3

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last, l, n = {}, 0, 0
        for r in range(len(s)):
            c = s[r]
            if l <= last.get(c, -1):
                l = last[c] + 1
            elif n <= r - l:
                n = r - l + 1
            last[c] = r
        return n

        N = len(set(list(s)))
        for i in range(N, 0, -1):
            for x in range(0, len(s) - i + 1):
                if i == max([len(set(s[x:x + i]))]):
                    return i
        return 0

        ret = 0
        kind = len(set(list(s)))
        for i in range(kind + 1)[::-1]:
            l = [len(set(s[x:][:i])) for x in range(len(s))]
            if l and i == max(l):
                ret = i
                break
        return ret
