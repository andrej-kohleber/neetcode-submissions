# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, low, heigh) -> bool:
            if not root:
                return True
            
            if not (low < root.val and root.val < heigh):
                return False
            
            return isValid(root.left, low, root.val) and isValid(root.right, root.val, heigh)
        
        return isValid(root, float("-inf"), float("inf"))


        

