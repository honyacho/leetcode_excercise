class Solution:
    def makePairAndRest(self, head):
        if not head.next:
            return (head, None)
        nextNext = head.next.next
        head.next.next = None
        return (head, nextNext)

    def reversePair(self, head):
        tmp1 = head
        tmp2 = head.next
        tmp2.next = tmp1
        tmp1.next = None
        return tmp2

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return head
        pr, tail = self.makePairAndRest(head)
        rev_pr = self.reversePair(pr) if pr.next else pr
        result = rev_pr
        ptr = rev_pr.next
        while tail and ptr:
            pr, tail = self.makePairAndRest(tail)
            ptr.next = self.reversePair(pr) if pr.next else pr
            ptr = ptr.next and ptr.next.next

        return result
