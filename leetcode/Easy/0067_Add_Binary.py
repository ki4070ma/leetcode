class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ret = ""
        length = max(len(a), len(b))
        kuriage = False
        a = a[::-1]
        b = b[::-1]
        for i in range(length):
            ret_val = 1 if kuriage else 0
            kuriage = False
            if len(a) > i and len(b) > i:
                #                print('a: {}, b: {}'.format(a[i], b[i]))
                ret_val += int(a[i]) + int(b[i])
            elif len(a) > i:
                #                print('a: {}'.format(a[i]))
                ret_val += int(a[i])
            elif len(b) > i:
                #                print('b: {}'.format(b[i]))
                ret_val += int(b[i])
            if ret_val > 1:
                kuriage = True
                ret_val = ret_val % 2
            ret = str(ret_val) + ret
        else:
            if kuriage:
                ret = "1" + ret
        return ret
