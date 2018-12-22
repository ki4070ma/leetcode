#!/usr/bin/python3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = self._convert(l1) + self._convert(l2)
        ret_l = []
        for n in list(str(sum)):
            ret_l.insert(0, eval(n))
        return ret_l

    def _convert(self, l):
        val = l.val
        next = l.next
        c = 10
        while next != None:
            val += c * next.val
            next = next.next
            c *= 10
        return val
