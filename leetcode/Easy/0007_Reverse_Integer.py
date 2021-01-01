#!/usr/bin/python3


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret_str = ""
        s = str(x)
        if len(s) == 1:
            return x
        minus_flg = True if s.startswith("-") else False
        s = s.split("-")[-1]
        print(s)
        count = 0
        for i in range(len(s), 0, -1):
            if s[i - 1] == "0":
                count += 1
            else:
                break
        s = s[: len(s) - count]
        for i in range(len(s), 0, -1):
            ret_str += s[i - 1]
        ret = -eval(ret_str) if minus_flg else eval(ret_str)
        if ret > pow(2, 31) - 1 or ret < -pow(2, 31):
            return 0
        return ret

        # Brute force
        ret_str = ""
        x_str = str(x)
        minus_flg = False
        for i in range(len(str(x)), 0, -1):
            #            print(x_str[i-1])
            if x_str[i - 1] == "-":
                minus_flg = True
                break
            elif x_str[i - 1] == "0":
                if len(ret_str) == 0:
                    ret_str = x_str[i - 1]
                elif ret_str == "0":
                    pass
                else:
                    ret_str += x_str[i - 1]
            elif x_str[i - 1] != "0":
                if ret_str == "0":
                    ret_str = x_str[i - 1]
                else:
                    ret_str += x_str[i - 1]
        ret = -eval(ret_str) if minus_flg else eval(ret_str)
        if ret > pow(2, 31) - 1 or ret < -pow(2, 31):
            return 0
        return ret
