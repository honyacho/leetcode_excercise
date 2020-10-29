# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        newNode = None
        if t1 and t2:
            newNode = TreeNode(t1.val + t2.val, self.mergeTrees(t1.left, t2.left), self.mergeTrees(t1.right, t2.right))
        elif t1:
            newNode = TreeNode(t1.val, self.mergeTrees(t1.left, None), self.mergeTrees(t1.right, None))
        elif t2:
            newNode = TreeNode(t2.val, self.mergeTrees(t2.left, None), self.mergeTrees(t2.right, None))
        return newNode