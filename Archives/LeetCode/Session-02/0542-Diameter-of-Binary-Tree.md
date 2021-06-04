# 542. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges
between them.

---

The length of the diameter of the binary tree here is defined as the longest
path between any two nodes - that may or may not pass through the root. Hence,
the problem can be solved recursively returning the maximum height from left
and right subtrees while at each depth, recording the maximum path length.

---

Python:

```python

class Solution542:

    def diameterOfTree(self, root):

        def helper(node):
            if not node:
                return 0
            # explore and returns maximum heights from left and right subtree
            l, r = helper(node.left), helper(node.right)
            self.result = max(self.result, l + r)
            return max(l, r) + 1

        self.result = 0
        helper(root)

        return self.result
```

