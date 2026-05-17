# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:                

        dummy = ListNode(0, None)
        cur = dummy        
        car = 0

        while l1 or l2 or car:
            # val1 = l1.val if l1 else 0
            # val2 = l2.val if l2 else 0

            # total = val1 + val2 + car
            # digit = total % 10


            
            v = (l1.val if l1 else 0) + (l2.val if l2 else 0) + car
            car = v // 10
            cur.next = ListNode(v % 10, None)
            cur = cur.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return dummy.next
   



