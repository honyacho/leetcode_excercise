# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.next_ = root
        while self.next_ and self.next_.left:
            self.stack.append(self.next_)
            self.next_ = self.next_.left

    def next(self) -> int:
        if not self.next_: return 0
        res = self.next_
        if self.next_.right:
            next_ = self.next_.right
            while next_.left:
                self.stack.append(next_)
                next_ = next_.left
            self.next_ = next_
        else:
            self.next_ = self.stack.pop() if self.stack else None
        return res.val

    def hasNext(self) -> bool:
        return True if self.next_ else False
