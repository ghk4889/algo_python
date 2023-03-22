# 23. Merge k Sorted Lists
import heapq
from typing import Optional, List

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# Output: [1,1,2,3,4,4,5,6]




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        root = result = ListNode()

        while heap:
            tupnode = heapq.heappop(heap)
            result.next = tupnode[2]
            result = tupnode[2]
            if tupnode[2].next:
                heapq.heappush(heap, (tupnode[2].next.val, tupnode[1], tupnode[2].next))

        return root.next
