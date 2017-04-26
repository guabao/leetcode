# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1

        if l1.val < l2.val:
            l0 = l = l1
            l1 = l1.next
        else:
            l0 = l = l2
            l2 = l2.next
        
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
                l = l.next
            else:
                l.next = l2
                l2 = l2.next
                l = l.next
        l.next = l1 if l1 else l2
        return l0
