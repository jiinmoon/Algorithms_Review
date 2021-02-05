# Path to Given Node

## Problem Description

    Given a Binary Tree A containing N nodes.

    You need to find the path from Root to a given node B.

## NOTE:

    No two nodes in the tree have same data values.
    You can assume that B is present in the tree A and a path always exists.


## Problem Constraints

    1 <= N <= 105
    1 <= Data Values of Each Node <= N
    1 <= B <= N



## Input Format

    First Argument represents pointer to the root of binary tree A.

    Second Argument is an integer B denoting the node number.



## Output Format

    Return an one-dimensional array denoting the path from Root to the node B in
    order.

---

## Approach:

We recursively traverse on the given tree, building the path for every node
that we seen. Once the target node has been found, we return our result.

O(n) in time and space complexity.

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
    
    ArrayList<Integer> result;
    
    public ArrayList<Integer> solve(TreeNode A, int B) 
    {
        this.result = new ArrayList<>();
        helper(A, B, new ArrayList<>());
        return this.result; 
    }
    
    private void helper(TreeNode node, int target, ArrayList<Integer> path)
    {
        if (Objects.isNull(node))
            return;
        
        if (node.val == target)
        {
            for (int val : path)
                this.result.add(val);
            this.result.add(node.val);
        }
        
        path.add(node.val);
        helper(node.left, target, path);
        helper(node.right, target, path);
        path.remove(path.size()-1);
    }
}
```
