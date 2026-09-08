# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        r = []
        q = deque([root])               
        while q:
            s = len(q)
            ls = []
            for i in range(s):
                n = q.popleft()
                if not n:
                    continue
                ls.append(n.val)
                q.append(n.left)
                q.append(n.right)
            if ls:                    
                r.append(ls)                        
        return r
        