# Balanced Binary Tree

    Given a binary tree, determine if it is height-balanced.

    Height-balanced binary tree : is defined as a binary tree in which the depth
    of the two subtrees of every node never differ by more than 1. 

    Return 0 / 1 ( 0 for false, 1 for true ) for this problem


---

## Approach:

We can modify height algorithm; recursively traverse down to the leaves and
start returning the height. At each node, we compare the returned maximum
heights from left and right subtree and check to see whether they are balanced.

O(n) in time complexity.

---

Python:

```python


class Solution:

    def isBalanced(self, root):
        
        def helper(node):
            if not node:
                return 0

            l, r = helper(node.left), helper(node.right)
            
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1

            return max(l, r) + 1

        return 1 if helper(node) != -1 else 0
```


