# 617. Merge Two Binary Trees

Given two binary trees and imagine that when you put one of them to cover the
other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two
nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.

---

Iterate on both trees; move over values from other if we can.

O(n) in both time and space complexity.

---

Python: Recursive.

```python

class Solution:

    def mergeTwo(self, p, q):
        if not (p and q):
            return p or q

        node = TreeNode(p.val + q.val)
        node.left = self.mergeTwo(p.left, q.left)
        node.right = self.mergeTwo(p.right, q.right)

        return node
```

Python: Iterative.

```python

class Solution:

    def mergeTwo(self, p, q):

        if not (p and q):
            return p or q

        stack = [(p, q)]

        while stack:

            curr1, curr2 = stack.pop()

            if not (curr1 and curr2):
                continue

            curr1.val += curr2.val

            if not curr1.left:
                curr1.left = curr2.left
            else:
                stack.append((curr1.left, curr2.left))

            if not curr1.right:
                curr1.right = curr2.right
            else:
                stack.append((curr1.right, curr2.right))

        return p
```
