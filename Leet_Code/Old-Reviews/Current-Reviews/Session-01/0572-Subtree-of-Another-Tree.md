572 Subtree of Another Tree
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

Python: tree traversal approach.

```python

class Solution:
    def isSameTree(self, s, t):
        if not (s and t):
            return s == t
        if s.val != t.val:
            return False
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

    def isSubtree(self, s, t):
        if not s:
            return False
        # traverse through s while performing comparison on each. 
        return self.isSameTree(s, t) or self.isSameTree(s.left, t) or self.isSameTree(s.right, t)
```

Python: codecs approach; it appears to be ~100 ms faster than other approach.

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
