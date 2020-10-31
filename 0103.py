from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list:
        result = []
        if not root: return result
        dq = deque([(root, 0)])

        while dq:
            node, depth = dq.popleft()
            if not depth < len(result):
                result.append([])
            result[depth].append(node.val)

            if node.left:
                dq.append((node.left, depth+1))
            if node.right:
                dq.append((node.right, depth+1))

        for i, r in enumerate(result):
            if i % 2: r.reverse()
        return result