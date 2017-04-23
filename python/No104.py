# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
		List = []
		if root != None:
		    List.append(root)
		depth = 0
		while List:
			depth += 1
			Current = []
			for node in List:
				if node.left:
					Current.append(node.left)
				if node.right:
					Current.append(node.right)
			List = Current
		return depth
