# Merge Two Binary Tree

## Problem Description

    Given two Binary Trees A and B, you need to merge them in a single binary tree.

    The merge rule is that if two nodes overlap, then sum of node values is the new
    value of the merged node.

    Otherwise, the non-null node will be used as the node of new tree.



## Problem Constraints

    1 <= Number of Nodes in A , B <= 105



## Input Format

    First argument is an pointer to the root of binary tree A.

    Second argument is an pointer to the root of binary tree B.



## Output Format

    Return a pointer to the root of new binary tree.

---

## Approach:

Recursively traverse down on both of the trees. At each depth, we create a new
node that is sum of both of the nodes. If we do not have two nodes, return
whichever is present. Repeat for left and right subtree. Alternatively, we can
do this inplace by using one of the tree as a base, and move over other tree.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def merge(self, A, B):

        if not (A and B):
            return A or B
        
        A.val += B.val

        A.left = self.merge(A.left, B.left)
        A.right = self.merge(A.right, B.right)

        return A

```
