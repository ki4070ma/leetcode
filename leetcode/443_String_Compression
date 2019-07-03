class Solution:
    def compress(self, chars: List[str]) -> int:
        prev_c = chars[0]
        count = 1
        ret = []
        for i, c in enumerate(chars[1:]):
            if prev_c == c:
                count += 1
            else:
                ret.append(prev_c)
                if count != 1:
                    for n in list(str(count)):
                        ret.append(n)
                prev_c = c
                count = 1
            if i == len(chars[1:]) - 1:
                ret.append(c)
                if count != 1:
                    for i in list(str(count)):
                        ret.append(i)
        if len(chars) == 1:
            import copy
            ret = copy.copy(chars)
        del chars[:]
        chars.extend(ret)
        return len(chars)
