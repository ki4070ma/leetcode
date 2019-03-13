#!/usr/bin/python3

class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        val1 = 0
        for i, x in enumerate(list(num1[::-1])):
            val1 += eval(x)*10**i
        val2 = 0
        for i, x in enumerate(list(num2[::-1])):
            val2 += eval(x)*10**i
        return str(val1*val2)
