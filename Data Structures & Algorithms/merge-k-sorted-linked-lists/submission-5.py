# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(minHeap, (lst.val, i, lst))

        dummy = ListNode()
        cur = dummy

        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
        
        return dummy.next
                
       
       
       
       
       
        # res = ListNode(0)
        # cur = res

        # while True:
        #     minVal = float('inf')
        #     minNode = -1
        #     for i in range(len(lists)):
        #         if not lists[i]:
        #             continue
        #         if lists[i].val < minVal:
        #             minVal = lists[i].val
        #             minNode = i
        #     if minVal == float('inf'):
        #         break
        #     cur.next = lists[minNode]
        #     lists[minNode] = lists[minNode].next
        #     cur = cur.next


        # return res.next