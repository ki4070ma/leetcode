class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ret = 0
        for x in range(len(s)):
            for y in range(len(s), x, -1):
                if self.chk_parentheses(s[x:y]):
                    if ret < len(s[x:y]):
                        ret = len(s[x:y])
                    break
                elif ret > len(s[x:y]):
                    break
        return ret

    def chk_parentheses(self, s: str) -> bool:
        stack = []
        for c in list(s):
            if c == '(':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if '(' not in stack:
                    return False
                if '(' == stack[-1]:
                    stack = stack[:-1]
                else:
                    return False
        if stack:
            return False
        return True  # Return True if stack is empty
