# 572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the
same structure and node values with a subtree of s. A subtree of s is a tree
consists of a node in s and all of this node's descendants. The tree s could
also be considered as a subtree of itself.

---

Two general approaches can be made here. One that can complete this process in
O(m + n) time complexity would be a method where we first raverse on the given
trees to retrieve all the nodes in order, then check whether one list can be
found in another. This however will require additional O(m + n) space as well.

Another approach is a recursive one where we simply perform check for whether
two trees are same from each of the node from one tree to another. This is
O(m^2) in time complexity but will be constant in space.

---

Python:

```python

class Solution:
    def isSubtreeOfAnother(self, p, q):
        if not p:
            return False
        return self.isSame(p, q) or self.isSubtreeOfAnother(p.left, q) or self.isSubtreeOfAnother(p.right, q)

    def isSame(self, p, q):
        if not (p or q):
            return p == q
        if not p.val == q.val:
            return False
        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
```
