# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        q = deque([root])
        while q:
            size = len(q)
            last = None
            for i in range(size):
                n = q.popleft()
                if not n:
                    continue
                q.append(n.left)
                q.append(n.right)
                last = n.val
            if last:                
                r.append(last)
        return r

        