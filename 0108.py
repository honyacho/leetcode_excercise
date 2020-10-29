# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        return self.sortedArrayToBSTImpl(nums, 0, len(nums))

    def sortedArrayToBSTImpl(self, nums: list, left: int, right: int) -> TreeNode:
        result = None
        if nums and left != right and left < len(nums):
            result = TreeNode(nums[(left+right)//2], self.sortedArrayToBSTImpl(nums, left, (left+right)//2), self.sortedArrayToBSTImpl(nums, (left+right)//2 + 1, right))
        return result
