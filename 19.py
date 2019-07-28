# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nth_before = None
        tail = head
        tail_pos = 0
        while tail.next:
            if tail_pos == n:
                nth_before = head
            tail = tail.next
            if nth_before:
                nth_before = nth_before.next
            tail_pos += 1
        if nth_before:
            nth_before.next = nth_before.next.next
        else:
            if n == tail_pos:
                head.next = head.next.next
            else:
                head = head.next
        return head
