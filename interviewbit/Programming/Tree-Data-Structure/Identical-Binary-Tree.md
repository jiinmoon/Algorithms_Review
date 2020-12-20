# Identical Binary Tree

    Given two binary trees, write a function to check if they are equal or not.

    Two binary trees are considered equal if they are structurally identical and
    the nodes have the same value.

    Return 0 / 1 ( 0 for false, 1 for true ) for this problem


## Approach:

Recursively traverse down on both of the tree in same directions; at each node
we compare their values. If either one of them does not exist, then other
should not also exist.

O(n) in time complexity.

---

Java:

```java
/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) {
 *      val = x;
 *      left=null;
 *      right=null;
 *     }
 * }
 */
public class Solution {
    
    public int isSameTree(TreeNode A, TreeNode B) { return (helper(A, B)) ? 1 : 0; }
    
    private boolean helper(TreeNode A, TreeNode B)
    {
        if (Objects.isNull(A) || Objects.isNull(B))
            return Objects.isNull(A) && Objects.isNull(B);
            
        if (A.val != B.val)
            return false;
            
        return helper(A.left, B.left) && helper(A.right, B.right);
    }
}

```
