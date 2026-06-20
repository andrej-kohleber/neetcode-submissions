# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.isSubTree = False
        self.dfs(root, subRoot)  
        return self.isSubTree      

    def dfs(self, root, subRoot) -> None:    
        if (self.isSameTree(root, subRoot)):
            self.isSubTree = True
            return
        if root:
            self.dfs(root.left, subRoot)
            self.dfs(root.right, subRoot)
        

    def isSameTree(self, root, subRoot) -> bool:
        if not root and not subRoot:
                return True
        if root and not subRoot:
            return False
        if not root and subRoot:
            return False
        
        return root.val == subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)