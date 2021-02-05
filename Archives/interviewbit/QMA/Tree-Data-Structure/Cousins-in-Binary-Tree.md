# Cousins in Binary Tree

Given a Binary Tree A consisting of N nodes.

You need to find all the cousins of node B.

NOTE:

Siblings should not be considered as cousins.
Try to do it in single traversal.
You can assume that Node B is there in the tree A.
Order doesn't matter in the output.

---

Use BFS to gather nodes level by level. If any node is found to be parent of
target node, we skip adding that node's child and return the current level
seen.

O(h) in time complexity where h in the depth to target node - O(n) in worst
case.

---

Python:

```python

from collections import deque

class Solution:

    def cousins(self, A, B):

        found, queue = False, deque([A])

        while queue and not found:
            
            m = len(queue)

            for _ in range(m):
                
                node = queue.popleft()

                if node.left and node.left.val == B or node.right and node.right.val == B:
                    found = True
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

        return [node.val for node in queue]
```
