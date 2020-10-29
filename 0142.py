# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        if not head: return None
        ptr_slow = head
        ptr_fast = head
        # first step
        while 1:
            if ptr_fast and ptr_fast.next:
                ptr_fast = ptr_fast.next.next
            else:
                return None
            if ptr_slow:
                ptr_slow = ptr_slow.next
            else:
                return None

            if ptr_fast == ptr_slow:
                break

        ptr_fast = head
        cnt = 0
        while 1:
            if ptr_fast == ptr_slow:
                print(cnt)
                return ptr_fast

            if ptr_fast:
                ptr_fast = ptr_fast.next
            else:
                return None

            if ptr_slow:
                ptr_slow = ptr_slow.next
            else:
                return None

            cnt += 1
