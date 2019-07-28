# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tl = ListNode(0)
        tl2 = None
        head = tl
        rest = 0

        while not (l1 == None and l2 == None):
            su = rest
            if l1: su += l1.val
            if l2: su += l2.val

            rest = su//10
            tl.val = su % 10
            tl.next = ListNode(0)
            
            tl2 = tl
            tl = tl.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if rest:
            tl.val = rest
        else:
            tl2.next = None
            
        return head
