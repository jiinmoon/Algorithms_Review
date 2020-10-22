# 572 Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the
same structure and node values with a subtree of s. A subtree of s is a tree
consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself.

---

There are several approaches but simpler approach with O(m + n) in time
complexity can be achieved by serializing or codifying the two given trees; and
perform substring search of one on the other. To do so, we perform tree
traversal.

---

Python:

```python

class Solution:
    def isSubtree(self, s, t):
        def serialize(node, path):
            if not node:
                path.append("None")
                return
            serialize(node.left, path + "," + str(node.val))
            serialize(node.right, path + "," + str(node.val))

        serialS, serialT = "", ""
        serialize(s, serialS)
        serialize(t, serialT)
        return serialT in serialS
```
