/*
Largest BST

You're given a binary tree. Your task is to find the size of the largest subtree within this binary tree that also satisfies the 
properties of a Binary Search Tree (BST). The size of a subtree is defined as the number of nodes it contains.

Note: A subtree of the binary tree is considered a BST if for every node in that subtree, the left child is less than the node, 
and the right child is greater than the node, without any duplicate values in the subtree.

Examples :

Input: root = [5, 2, 4, 1, 3]
Root-to-leaf-path-sum-equal-to-a-given-number-copy
Output: 3
Explanation:The following sub-tree is a BST of size 3

Input: root = [6, 7, 3, N, 2, 2, 4]
Output: 3
Explanation: The following sub-tree is a BST of size 3:

Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 105
*/

//Code
class Solution {

    static class Info {
        int min, max, size;
        Info(int min, int max, int size) {
            this.min = min;
            this.max = max;
            this.size = size;
        }
    }
    static Info solve(Node root) {
        if (root == null)
            return new Info(Integer.MAX_VALUE, Integer.MIN_VALUE, 0);
        Info left = solve(root.left);
        Info right = solve(root.right);
        if (left.max < root.data && root.data < right.min) {
            return new Info(
                Math.min(root.data, left.min),
                Math.max(root.data, right.max),
                left.size + right.size + 1
            );
        }
        return new Info(Integer.MIN_VALUE, Integer.MAX_VALUE,
                        Math.max(left.size, right.size));
    }
    static int largestBst(Node root) {
        return solve(root).size;
    }
}