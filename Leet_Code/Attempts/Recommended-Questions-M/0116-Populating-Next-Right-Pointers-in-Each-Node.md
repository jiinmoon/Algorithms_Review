# 116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and
every parent has two children.

---

We can approach this problem with a BFS where it will traverse on the given
binary tree in level order fashion - thus, at each depth, we can populate the
next right pointers.

---

Python:

```python

class Solution:
    def connect(self, root):
        if not root:
            return None

        q = [root]
        while q:
            temp = list()
            prev = None
            for node in q:
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    temp.append(node.left)
                    temp.append(node.right)
            q = temp
        return root
```
