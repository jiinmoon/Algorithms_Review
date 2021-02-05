# Next Pointer Binary Tree

Populate each next pointer to point to its next right node. If there is no next
right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

---

Use BFS to iterate on the given tree in level order fashion. Then, we can set
the each node on the same level by next node in the queue.

O(n) in time complexity and O(log(n)) in space as there can only be log(n)
bounded number of nodes in any given depth.

---

Python:

```python

class Solution:

    def connect(self, root):

        if not root:
            return

        queue = [ root ]

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
```

