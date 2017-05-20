# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        h0 = head
        
        left = h0
        right = h0.next
        
        while right:
            if right.val == left.val:
                right = right.next
                left.next = right
            else:
                left = right
                right = right.next
        return h0
