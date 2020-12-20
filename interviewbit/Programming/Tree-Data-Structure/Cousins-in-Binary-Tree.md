# Cousins in Binary Tree

## Problem Description

    Given a Binary Tree A consisting of N nodes.

    You need to find all the cousins of node B.

## NOTE:

    Siblings should not be considered as cousins.
    Try to do it in single traversal.
    You can assume that Node B is there in the tree A.
    Order doesn't matter in the output.


## Problem Constraints

    1 <= N <= 105
    1 <= B <= N


## Input Format

    First Argument represents the root of binary tree A.

    Second Argument is an integer B denoting the node number.



## Output Format

    Return an integer array denoting the cousins of node B.

    NOTE: Order doesn't matter.

---

## Approach:

We can use BFS algorithm to discover the nodes depth after another. Once we
find the node that has the target node as a child, we skip over adding that
node's children as they are siblings and stop our search to return the last
level that we have discovered.

O(n) in time complexity.

---

Python:

```python

from collections import deque

class Solution:
    
    def solve(self, A, B):

        found, queue = False, deque([A])

        while not found and queue:

            m = len(queue)

            for _ in range(m):

                node = queue.popleft()

                if node.left and node.left.val == B or node.right and node.right.val == B:
                    found = True
                    continue
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

        return [node.val for node in queue]
```
