# Path to Given Node

Given a Binary Tree A containing N nodes.

You need to find the path from Root to a given node B.

NOTE:

No two nodes in the tree have same data values.
You can assume that B is present in the tree A and a path always exists.

---

Python:

```python

class Solution:

    def solve(self, A, B):

        def _traverse(node, path):
            if not node:
                return
            elif node.val == B:
                self.result = path + [node.val]
                return
            else:
                _traverse(node.left, path + [node.val])
                _traverse(node.right, path + [node.val])

        self.result = []

        _traverse(A, [])

        return self.result
```

