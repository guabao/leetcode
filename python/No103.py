# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        l = [root]
        values = []
        i = 0
        flag = True
        while l:
            l_new = []
            values_new = []
            for li in l:
                values_new.append(li.val)
                if li.left:
                    l_new.append(li.left)
                if li.right:
                    l_new.append(li.right)
            if flag:
                values.append(values_new)
            else:
                values.append(values_new[::-1])
            l = l_new
            flag = not flag
            
        return values
