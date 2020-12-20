# Remove Half Nodes

## Problem Description

    Given a binary tree A with N nodes.

    You have to remove all the half nodes and return the final binary tree.

## NOTE:

    Half nodes are nodes which have only one child.
    Leaves should not be touched as they have both children as NULL.


## Problem Constraints

    1 <= N <= 105



## Input Format

    First and only argument is an pointer to the root of binary tree A.



## Output Format

    Return a pointer to the root of the new binary tree.

---


## Approach:

The problem here is about collapsing the tree to remove the nodes that only has
a single child down to the leaf nodes.

Using recursion, on every node that we visit, we try to collapse down as much
as possible - that is, so long as the node has a single child, we move down.
Then, we fix the node's left and right subtree as a recursive call to itself so
that we only return the nodes which are not half nodes.

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
    
    public TreeNode solve(TreeNode A) 
    {
        if (Objects.isNull(A) || Objects.isNull(A.left) && Objects.isNull(A.right))
            return A;
        
        while (true)
        {
            if (Objects.isNull(A.left) && Objects.nonNull(A.right))
                A = A.right;
            else if (Objects.nonNull(A.left) && Objects.isNull(A.right))
                A = A.left;
            else
                break;
        }
        
        A.left = solve(A.left);
        A.right = solve(A.right);
        
        return A;
    }
}

```

Java:

```java

public class Solution {

    public TreeNode solve(TreeNode A) 
    {
        if (Objects.isNull(A) || Objects.isNull(A.left) && Objects.isNull(A.right))
            return A;
            
        if (Objects.isNull(A.left))
            return solve(A.right);
        
        if (Objects.isNull(A.right))
            return solve(A.left);
        
        A.left = solve(A.left);
        A.right = solve(A.right);
        
        return A;
    }
}
```
