# 156. Binary Tree Upside Down

Given the root of a binary tree, turn the tree upside down and return the new
root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.


---


We can recursively fix this tree upside down by first visiting the leftmost
node in the tree. This is the new root of our binary tree (and every subtree).
Here, we apply the steps as laid out above. The right most child starting from
our new root becomes the left child, and current root becomes the right child.
To avoid cycle, root's original pointers should be set to null.

This would be O(n) in time complexity.

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
class Solution156 {

    public TreeNode upsideDownBinaryTree(TreeNode root) 
    {
        if (Objects.isNull(root) || Objects.isNull(root.left))
            return root;
        
        TreeNode newRoot = upsideDownBinaryTree(root.left);

        TreeNode curr = newRoot;
        for (; Objects.nonNull(curr.right); curr = curr.right);

        curr.left = root.right;
        curr.right = root;

        root.left = null;
        root.right = null;
        
        return newRoot;
    }
}
```
