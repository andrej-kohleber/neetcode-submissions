# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:            
        head = self.rec(head, head.next)    

    def rec(self, root: ListNode, cur: ListNode) -> ListNode:
        if not cur:
            return root
        
        root = self.rec(root, cur.next)
        if not root:
            return None
        
        tmp = None
        if root == cur or root.next == cur:
            cur.next = None
        else:
            tmp = root.next
            root.next = cur
            cur.next = tmp
        
        return tmp
    
    

        
        