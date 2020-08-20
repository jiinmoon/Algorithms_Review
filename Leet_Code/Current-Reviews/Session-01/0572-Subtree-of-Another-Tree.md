572 Sbutree of Another Tree
===========================

Given two non-empty binary trees s and t, check whether tree t has exactly the
same structure and node values with a subtree of s. A subtree of s is a tree
consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself.

---

We could perform a tree traversal and once we encounter a same starting node as
root of t, we can perform `isSameTree` operation downwards.

But simply, we can just serialize two trees, and perform pattern matching.

---

Python:

```python
class Solution:
    def isSubtree(self, s, t):
        sSerial, tSerial = [], []

        def serialize(node, path)
            if not node:
                path += ["null"]
                return
            path += ["," + str(node.val))]
            serialize(node.left, path)
            serialize(node.right, path)

        serialize(s, sSerial)
        serialize(t, tSerial)
        sSerial = "",join(sSerial)
        tSerial = "",join(tSerial)
        return tSerial in sSerial
```
