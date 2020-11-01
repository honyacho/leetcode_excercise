# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "TN={}({}, {})".format(self.val, self.left or "_", self.right or "_")

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if not preorder: return None
        return self.dfs(preorder, inorder, 0, 0, len(preorder))[0]

    def dfs(self, preorder: list, inorder: list, root: int, ileft: int, iright: int) -> (TreeNode, int):
        if not ileft < iright: return None, 0
        value = preorder[root]
        node = TreeNode(value)

        try:
            mid = inorder.index(value, ileft, iright)

            left, left_size = self.dfs(preorder, inorder, root + 1, ileft, mid)
            node.left = left
            right, right_size = self.dfs(preorder, inorder, root + left_size + 1, mid+1, iright)
            node.right = right
            return node, left_size + right_size + 1
        except:
            return None, 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.buildTree([3],[3]))
    print(sol.buildTree([3,9,20,15,7],[9,3,15,20,7]))
    print(sol.buildTree([1,2,3],[2,3,1]))