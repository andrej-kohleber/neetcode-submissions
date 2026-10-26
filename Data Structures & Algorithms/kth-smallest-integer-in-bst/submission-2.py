# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list = []
        def dfs(node, k) -> None:
            if not node:
                return
            
            dfs(node.left, k)
            list.append(node.val)
            print(str(len(list)) + " " + str(k))
            if (len(list) == k):
                return
            dfs(node.right, k)
        
        dfs(root, k)
        return list[k-1]

        