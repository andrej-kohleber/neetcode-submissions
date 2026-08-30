# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        rs = []

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                n = q.popleft()
                if n:
                    level.append(n.val)                
                    q.append(n.left)                
                    q.append(n.right)
            if level:
                rs.append(level)

        
        return rs









        # level = []
        # while queue:                        
        #     node = queue.popleft()    
        #     level.append(node)
        
        # ls = []        
        # for n in level:
        #     ls.append(n.val)
        #     if n.left:
        #         queue.append(n.left)
        #     if n.right:
        #         queue.append(n.right)                        
        
        # rs.append(ls)            

        # return rs

        