class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        d = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'],
             5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'],
             8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        l = []
        for i in digits:
            l.append(d[int(i)])
#        print(l)
        ret = []
        import itertools
        for val in itertools.product(*l):
            ret.append(''.join(val))
        return ret
