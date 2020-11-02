# 572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the
same structure and node values with a subtree of s. A subtree of s is a tree
consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself.

---

There are two approaches to this problem. First approach is that we can
serialize two trees into a string format and check to see whether one is found
on another. This would be O(n + m) in time complexity, but it would also
require additional space.

Another approach is the recursive one where we would traverse on the s; and
starting from each of the node, we try to match the subtree of s to t. This
will increase the time complexity, but would not require additional space.

---

Python:

```python

class Solution:
    def isSubtree(self, s, t):
        if not s:
            return False
        return self.isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, s, t):
        if not (s or t):
            return s == t
        if s.val != t.val:
            return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
```
