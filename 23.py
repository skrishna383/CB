class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        a = []

        if(len(lists)>0):
            for i in range(len(lists)):
                if lists[i]:
                    heapq.heappush(a, (lists[i].val, i))
                    lists[i] = lists[i].next

            while a:
                val, i = heapq.heappop(a)
                tail.next = ListNode(val)
                tail = tail.next
                if lists[i]:
                    heapq.heappush(a, (lists[i].val, i))
                    lists[i] = lists[i].next

            return dummy.next