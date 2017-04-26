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
        
        h1 = h2 = head
        for _ in xrange(n):
            h2 = h2.next
            
        if not h2:
            return head.next
        
        while not h2.next is None:
            h2 = h2.next
            h1 = h1.next
        
        h1.next = h1.next.next
        
        return head
