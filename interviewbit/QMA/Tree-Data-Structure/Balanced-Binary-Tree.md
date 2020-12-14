# Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

 Height-balanced binary tree : is defined as a binary tree in which the depth
 of the two subtrees of every node never differ by more than 1. 

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

---

We can check for balance while computing the height of the binary tree. At each
node, we compare the height returned from left and right subtrees; if they
differ by more than one, we have our answer.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def isBalanced(self, root):

        def _check(node):
            
            nonlocal result

            if not node:
                return 0

            l, r = _check(node.left), _check(node.right)

            if abs(l - r) > 1:
                result = 0

            return max(l, r) + 1

        result = 1
        _check(root)

        return result
```
