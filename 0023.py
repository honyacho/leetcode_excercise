import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        pq = []
        head = None
        curr = None
#         initialize priority queue
        for i, lis in enumerate(lists):
            if lis:
                heapq.heappush(pq, (lis.val, i))
#         set head
        if not pq: return None
        val, i = heapq.heappop(pq)
        lis = lists[i]
        curr = lis
        head = lis
        if lis.next:
            lists[i] = lis.next
            heapq.heappush(pq, (lists[i].val, i))

#         main loop
        while pq:
            val, i = heapq.heappop(pq)
            lis = lists[i]
            curr.next = lis
            curr = curr.next
            if lis.next:
                lists[i] = lis.next
                heapq.heappush(pq, (lists[i].val, i))
        
        return head
