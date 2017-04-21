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
        digit = l1.val + l2.val
        ten, one = divmod(digit, 10)
        r0 = ListNode(one)
        rr = r0
        flag = (not l1.next is None) or (not l2.next is None) or (ten > 0)
        while flag:
            l11 = l1.next
            l22 = l2.next
            val_l1 = l11.val if not l11 is None else 0
            val_l2 = l22.val if not l22 is None else 0
            ten, one = divmod(val_l1 + val_l2 + ten, 10)
            r1 = ListNode(one)
            r0.next = r1
            if not l11 is None:
                l1 = l11
            if not l22 is None:
                l2 = l22
            flag = (not l1.next is None) or (not l2.next is None) or (ten > 0)
            r0 = r1
        return rr
