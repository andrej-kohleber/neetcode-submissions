# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node = None
        for i in range(len(lists)):
            node = self.mergeTwoLists(node, lists[i])


        return node
    
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        res = ListNode()
        cur = res

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 or list2
        return res.next
    
        


                
       
       
       
       
       
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