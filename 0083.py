# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        st = set()
        while head:
            if head in st:
                return True
            else:
                st.add(head)
                head = head.next
        return False