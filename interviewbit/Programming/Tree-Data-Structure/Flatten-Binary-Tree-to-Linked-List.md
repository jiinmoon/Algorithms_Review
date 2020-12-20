# Flatten Binary Tree to Linked List

    Given a binary tree, flatten it to a linked list in-place.

---

## Approach:

Step by step, we need to think about what we should do about at each node.

For every node that we visit, we wish to move over the left subtree unto right.
But we have a problem when current node already has a right subtree, which will
be discarded. Hence, we should first find the rightmost node on the left
subtree, and move over the current node's right subtree. And then move over the
left subtree to current node's right.

O(n) in time complexity.

---

Python:

```python

class Solution:

    def flatten(self, root):

        if not root:
            return None

        curr = root

        while curr:

            # need to move over left subtree to right
            while curr.left:
                
                # first, find the right most node on the left subtree
                rightMostNode = curr.left
                while rightMostNode.right:
                    rightMostNode = rightMostNode.right
                
                # move over current node's right subtree to right of right most node found
                rightMostNode.right = curr.right

                # move over left subtree to right
                curr.right = curr.left

                # delete duplicate entry into left subtree
                curr.left = None

            curr = curr.right

        return root
```
