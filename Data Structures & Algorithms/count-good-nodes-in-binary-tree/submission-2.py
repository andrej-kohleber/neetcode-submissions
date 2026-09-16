# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.n = 0
        max = float('-inf')

        def dfs(node, max_val):
            if not node:
                return
            if node.val >= max_val:
                self.n += 1
                max_val = node.val
            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, max)
        return self.n


        