# Vertical Order Traversal of Binary Tree

## Problem Description

    Given a binary tree A consisting of N nodes, return a 2-D array denoting the
    vertical order traversal of A.

    Go through the example and image for more details.

## NOTE:

    If 2 or more Tree Nodes shares the same vertical level then the one with
    earlier occurence in the pre-order traversal of tree comes first in the output.
    Row 1 of the output array will be the nodes on leftmost vertical line similarly
    last row of the output array will be the nodes on the rightmost vertical line.


## Problem Constraints

    0 <= N <= 104

## Input Format

    First and only argument is an pointer to root of the binary tree A.



## Output Format

    Return a 2D array denoting the vertical order traversal of A.

---

## Approach:

Use level order traversal, and record each of the visited node by their
x-coordinates in the hashmap. In the end, we can retrieve the vertical order by
going through the hashmap by its ordered key list.

Time complexity of O(n * log(n)) due to sorting of the keys involved.

---

Python:

```python

from collections import defaultdict, deque

class Solution:

    def verticalOrderTraversal(self, root):

        if not root:
            return []

        record = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            
            curr, x = queue.popleft()

            if not curr:
                continue
            
            record[x].append(curr)

            queue.append((curr.left, x - 1))
            queue.append((curr.right, x + 1))
        
        result = []

        for x in sorted(record.keys()):
            result.append(record[x])

        return result
```
