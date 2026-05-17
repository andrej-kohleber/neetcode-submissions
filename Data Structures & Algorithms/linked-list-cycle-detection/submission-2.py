# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    

        slow = head
        if not head:
            return False

        fast = head.next if head.next != None else None
        while slow:
            if fast == None or fast.next == None or fast.next.next == None:
                return False
            
            if fast == slow:
                return True

            slow = slow.next
            fast = fast.next.next




        return False
        