#!/usr/bin/python3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Count length of list
        count = 0
        p = head
        while p != None:
            count += 1
            p = p.next

        # Remove target num
        p = head
        target_num = count - n
        idx = 0  # reset
        ret = []
        while p != None:
            if idx == target_num:
                idx += 1
                p = p.next
                continue
            ret.append(p.val)
            p = p.next
            idx += 1
        return ret
