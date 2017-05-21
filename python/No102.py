# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        l = [root]
        values = []
        i = 0
        while l:
            l_new = []
            values_new = []
            for li in l:
                values_new.append(li.val)
                if li.left:
                    l_new.append(li.left)
                if li.right:
                    l_new.append(li.right)
            values.append(values_new)
            l = l_new
            
        return values
