class Solution:
    def defangIPaddr(self, address: str) -> str:
        ret = ''
        for n in address:
            if n == '.':
                ret += '[.]'
            else:
                ret += n
        return ret
        return '[.]'.join(address.split('.'))  # the fastest
        return address.replace('.', '[.]')
