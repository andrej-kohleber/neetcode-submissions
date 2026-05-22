# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            listNodes = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                listNodes.append(self.mergeTwoLists(l1, l2))
            lists = listNodes



        return lists[0]
    
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