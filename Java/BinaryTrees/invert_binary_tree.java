/*
	Invert a binary Tree
    Author: Nikhil Kumar Mengani 
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
         if(root == null){
            return root;
        }
        TreeNode tempNode = root.left;
        root.left = invertTree(root.right);
        root.right =invertTree(tempNode);
        return root;
    }
}