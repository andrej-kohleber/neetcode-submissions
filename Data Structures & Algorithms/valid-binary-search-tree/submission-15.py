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

    # def dfs(self, node, l, h) -> None:
    #     if not node or not self.valid:
    #         return
        
    #     if node.val <= l or node.val >= h:
    #         self.valid = False
        
    #     self.dfs(node.left, l, node.val)
    #     self.dfs(node.right, node.val, h)


    def dfs(self, node, l, h) -> None:
        if not node or not self.valid:
            return
        
        if node.val <= l or node.val >= h:
            self.valid = False
            # return  # Stop deep traversal immediately if invalid
        
        # Left child: lower bound remains 'l', upper bound drops to 'node.val'
        self.dfs(node.left, l, node.val)
            
            # Right child: lower bound rises to 'node.val', upper bound remains 'h'
        self.dfs(node.right, node.val, h)


        

