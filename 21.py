# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        curr = None
        if l1 and l2:
            if l1.val < l2.val:
                head = l1
                l1 = l1.next
                curr = head
            else:
                head = l2
                l2 = l2.next
                curr = head
        elif l2:
            return l2
        elif l1:
            return l1
        else:
            return None
            
            
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    curr = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    curr = l2
                    l2 = l2.next
            else:
                if l1:
                    curr.next = l1
                    return head
                else:
                    curr.next = l2
                    return head
        return head
