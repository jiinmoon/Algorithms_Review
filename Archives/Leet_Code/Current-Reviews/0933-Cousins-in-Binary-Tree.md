# 933. Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth
k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have
different parents.

We are given the root of a binary tree with unique values, and the values x and
y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are
cousins.

---

We recursively traverse down looking for two nodes. We record the depth where
they have been found. We early exit by checking current depth has exceeded the
recorded depth. If node is found to be either of the target nodes, we record
the depth and check whether they have been found at the same level.

We also check for whether they have been found at different parent by checking
aginst where they have been found against the parent depth of + 1.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def isCousins(self, root, x, y):

        def search(node, currDepth):

            nonlocal isCousin, foundDepth, x, y

            if not node:
                return False
            
            # no point in traversing further down the path
            if foundDepth and foundDepth <= currDepth:
                return False

            # current node is either target
            # check their depth
            if node.val in {x, y}:
                # first time we seen? record the depth
                if not foundDepth:
                    foundDepth = currDepth
                # otherwise, they should have been found at same depth
                return foundDepth == currDepth

            # recursively search for two targets
            l, r = search(node.left, currDepth+1), search(node.right, currDepth+1)

            # both have been found, they should not share same parent
            if l and r and foundDepth == currDepth + 1:
                isCousin = True
            # if either one is found, propagate upward
            return l or r
        
        isCousin, foundDepth = False, None
        search(root, 0)

        return isCousin
```
