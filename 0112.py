# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sm: int, current: int = 0) -> bool:
        if not root: return False
        res = False
        if root.right or root.left:
            if root.left:
                res = res or self.hasPathSum(root.left, sm, current+root.val)
            if root.right:
                res = res or self.hasPathSum(root.right, sm, current+root.val)
        else:
            return sm == current + root.val
        return res