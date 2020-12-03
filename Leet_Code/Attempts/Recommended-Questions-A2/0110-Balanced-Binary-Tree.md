# 110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in
height by no more than 1.

---

We first recursively traverse down to the leaves of the tree. Starting from
here, we return the maximum height along this path. If we find that absolute
difference between height returned from left and right subtrees differ by more
than 1, we determine that tree is not balaned; otherwise, we continue to return
height.

Time complexity would be typical O(n).

---

Java:

```java

class Solution110 {

    public boolean isBalanced(TreeNode root)
    {
        return (root == null) ? true : checkBalance(root) != -1;
    }

    private int checkBalance(TreeNode node)
    {
        if (node == null) 
            return 0;

        int l = checkBalance(node.left);
        int r = checkBalance(node.right);

        if (l == -1 || r == -1 || Math.abs(l - r) > 1)
            return -1;

        return Math.max(l, r) + 1;
    }
}

```
