/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) {
            return List.of();
        }

        List<List<Integer>> rs = new ArrayList<>();
        Queue<TreeNode> q = new ArrayDeque<>();
        q.offer(root);

        while (!q.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int qLen = q.size();
            for (int i = 0; i < qLen; i++) {
                TreeNode n = q.poll();
                if (n != null) {
                    level.add(n.val);
                    if (n.left != null) {
                        q.offer(n.left);
                    }
                    if (n.right != null) {
                        q.offer(n.right);
                    }                    
                }
            }
            if (!level.isEmpty()) {
                rs.add(level);
            }            
        }
        
        return rs;
    }
}
