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
        elif not head.next:
            return head
        else:
            h0 = ListNode(None)
            h0.next = head
            h1 = h0
            h2 = head
            while h2.next:
                if h2.next.val == h2.val:
                    while h2.next.val == h2.val:
                        h2 = h2.next
                        if not h2.next:
                            h1.next = None
                            break
                    h2 = h2.next
                    h1.next = h2
                else:
                    h1 = h2
                    h2 = h2.next
                if not h2:
                    break
        return h0.next
