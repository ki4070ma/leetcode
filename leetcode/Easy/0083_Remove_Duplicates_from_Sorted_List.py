# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        current = head.next
        prev = head

        while current is not None:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                current = current.next
                prev = prev.next
        return head
