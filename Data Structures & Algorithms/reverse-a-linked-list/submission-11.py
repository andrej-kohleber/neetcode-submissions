# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        dummy = ListNode(0, None)
        while node:
           tmp = node.next
           node.next = dummy.next
           dummy.next = node
           node = tmp
        
        return dummy.next
        