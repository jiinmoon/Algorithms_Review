116 Populating Next Right Pointers in Each Node
===============================================

Give a perfect binary tree where all leaves are one thsame level, and every
parent has two children, populate each next pointer to point to its next right
node; if it doesn't exist, should point at `null`.

---

Perform BFS traversal - since it traverses in level-order, once we retrieve all
the level, we can start to populate it as we examine. The time complexity
should be O(v + e).

---

Python:

```python

class Solution:
    def connect(self, root):
        if not root:
            return None

        q = [root]
        while q:
            nextq = list()
            prevNode = None
            for currNode in q:
                if prevNode:
                    prevNode.next = currNode
                prevNode = currNode
                if currNode.left:
                    nextq.append(currNode.left)
                    nextq.append(currNode.right)
            q = nextq

        return root
```
