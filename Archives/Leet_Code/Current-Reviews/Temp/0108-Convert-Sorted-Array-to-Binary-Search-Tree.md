# 108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to
a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.

---

To generate a height-balanced BST, we should take a root of mid-element - and
this definition applies recursively. Current node's left subtree values are to
the left of mid value and vice versa. O(n) in time complexity.

---

Java:

```java

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
class Solution108 {
    private int[] nums;
    
    private TreeNode buildBST(int l, int r)
    {
        if (l > r)
            return null;
        
        int mid = l + (r - l) / 2;
        
        TreeNode node = new TreeNode(this.nums[mid]);
        node.left = buildBST(l, mid - 1);
        node.right = buildBST(mid + 1, r);
        
        return node;
    }
    
    public TreeNode sortedArrayToBST(int[] nums) 
    {
        this.nums = nums;
        return buildBST(0, nums.length-1);
    }
}

```
