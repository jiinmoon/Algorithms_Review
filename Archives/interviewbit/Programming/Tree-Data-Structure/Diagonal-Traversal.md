# Diagonal Traversal

## Problem Description

    Consider lines of slope -1 passing between nodes.

    Given a Binary Tree A containing N nodes, return all diagonal elements in
    a binary tree belonging to same line.

## NOTE:

    See Sample Explanation for better understanding.
    Order does matter in the output.
    To get the same order as in the output traverse the tree same as we do in
    pre-order traversal.


## Problem Constraints

    0 <= N <= 105

## Input Format

    First and only Argument represents the root of binary tree A.

## Output Format

    Return a 1D array denoting the diagonal traversal of the tree.

---

We use queue to maintain the nodes to revisit; first, for each node, we should
traverse as far right as possible, diagonally down. While doing so, if there
are any left subtree, we should save it in the stack to revisit.

O(n) in time complexity.

---

Python:

```python

from collections import deque

class Solution:

    def diagonalTraversal(self, root):

        queue = deque([root])
        result = list()

        while queue:
            
            curr = queue.popleft()

            while curr:
                
                result.append(curr.val)

                if curr.left:
                    queue.append(curr.left)

                curr = curr.right

        return result
```
