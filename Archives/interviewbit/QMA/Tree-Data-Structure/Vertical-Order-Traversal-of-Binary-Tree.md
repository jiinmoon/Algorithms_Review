# Vertical Order Traversal of Binary Tree

Given a binary tree A consisting of N nodes, return a 2-D array denoting the
vertical order traversal of A.

Go through the example and image for more details.

NOTE:

If 2 or more Tree Nodes shares the same vertical level then the one with
earlier occurence in the pre-order traversal of tree comes first in the output.
Row 1 of the output array will be the nodes on leftmost vertical line similarly
last row of the output array will be the nodes on the rightmost vertical line.

---

Use hashmap to record all nodes belong under same column or x-coordinates.
After BFS, collect the nodes by sorted column order.

O(n) in time and space complexity.

---

Python:

```python

from collections import defaultdict

class Solution:

    def verticalOrderTraversal(self, root):

        d = defaultdict(list)
        q = [(root, 0)]

        while q:
            
            temp = []
            for node, x in q:
                if not node:
                    continue
                d[x].append(node.val)
                temp.append((node.left, x - 1))
                temp.append((node.right, x + 1))

            q = temp

        result = []
        for x in sorted(d.keys()):
            result.append(d[x])

        return result 
```
