# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True
        self.dfs(root, float("-inf"), float("inf"))
        return self.valid

    def dfs(self, node, l, h) -> None:
        if not node:
            return
        
        if node.val <= l or node.val >= h:
            self.valid = False
        
        self.dfs(node.left, l, node.val)
        self.dfs(node.right, node.val, h)


        

