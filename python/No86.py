# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left = ListNode(None)
        right = ListNode(None)
        
        l0 = left
        r0 = right
        h = head
        while h:
            if h.val < x:
                left.next = h
                left = left.next
            else:
                right.next = h
                right = right.next
            h = h.next
        left.next = r0.next
        right.next = None
        return l0.next
