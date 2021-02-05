# Populate Next Right Pointers Tree

    Populate each next pointer to point to its next right node. If there is no next
    right node, the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.

    Note:

    You may only use constant extra space.

---

## Approach:

Use BFS; for every level, we set the previous node to next node as we examine
them for next level.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def connect(self, root):

        if not root:
            return None

        queue = [root]

        while queue:
            
            prev, temp = None, []

            for node in queue:
                if prev:
                    prev.next = node
                prev = node

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            queue = temp

        return root
```
