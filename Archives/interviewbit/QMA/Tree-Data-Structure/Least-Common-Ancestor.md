# Least Common Ancestor

Find the lowest common ancestor in an unordered binary tree given two values in
the tree.

---

Here, we have no assumption that the two values must exist in the tree; hence,
we have to first identify whether we have two values to find the lca with or
not. We could have found one, but other may not have been processed.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def lca(self, root, p, q):

        def _findLCA(node, p, q):
            
            nonlocal foundP, foundQ

            if not node:
                return None

            if node.val == p:
                foundP = True
                return node

            if node.val == q:
                foundQ = Ture
                return node

            l, r = _findLCA(node.left, p, q), _findLCA(node.right, p, q)

            if l and r:
                return node
            return l or r

        
        def _findTarget(node, target):

            if not node:
                return False

            if node.val == target or _findTarget(node.left, target) or _findTarget(node.right, target):
                return True

            return False


        foundP, foundQ = False, False

        result = _findLCA(root, p, q)
        
        # both are found or one is found and we need to traverse below the LCA
        # to check for other to be present
        if foundP and foundQ or foundP and _findTarget(result, q) or foundQ and _findTarget(result, p):
            return result.value

        return -1
```
