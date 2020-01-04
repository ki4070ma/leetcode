#!/usr/bin/python3

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('(') != s.count(')') or s.count('{') != s.count('}') or s.count('[') != s.count(']'):
            return False

        stack = []
        left_gp = {'(': ')', '{': '}', '[': ']'}
        right_gp = {')': '(', '}': '{', ']': '['}

        for c in list(s):
            if c in left_gp.keys():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if right_gp[c] not in stack:
                    return False
                if right_gp[c] == stack[-1]:
                    stack = stack[:-1]
                else:
                    return False
        return True
