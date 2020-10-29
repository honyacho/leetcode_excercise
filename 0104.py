# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root, depth = 0, max_depth = 0) -> int:
        if root:
            l_max_depth = self.maxDepth(root.left, depth+1, max_depth)
            r_max_depth = self.maxDepth(root.right, depth+1, max_depth)
            return max(l_max_depth, r_max_depth)
        else:
            return depth