# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if not head: return False
        ptr_slow = head
        ptr_fast = head
        # first step
        while 1:
            if ptr_fast and ptr_fast.next:
                ptr_fast = ptr_fast.next.next
            else:
                return False
            if ptr_slow:
                ptr_slow = ptr_slow.next
            else:
                return False

            if ptr_fast == ptr_slow:
                return True
