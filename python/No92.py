# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        h0 = ListNode(None)
        h0.next = head
        i = 1
        h = h0
        while i < m:
            i += 1
            h = h.next
        h_pre = h
        h_start = h.next
        hh0 = h_start
        hh1 = h_start.next
        i = i + 1
        while i < n:
            hh2 = hh1.next
            hh1.next = hh0
            hh0 = hh1
            hh1 = hh2
            i += 1
        h_end = hh1
        h_pre.next = h_end
        h_start.next = h_end.next
        hh1.next = hh0
        return h0.next
