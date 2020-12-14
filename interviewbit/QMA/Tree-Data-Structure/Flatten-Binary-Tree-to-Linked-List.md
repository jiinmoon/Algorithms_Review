# Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

---

Let's think about this problem as we iterate down to visit each node.

First, for current node, its left subtree should be attached to the right. But,
we may already have right subtrees. Thus, the right subtree should be rightmost
node to current node's left subtree.

Let's visualize with an example:

```
                    1
                /       \
            2               5
        /       \               \
    3               4               6


Given above tree, let's start at root of "1".

First, we should find the rightmost node to the left of the root which is "4".

To the right of 4, we can attach the root's right subtree ("5").

                    1
                /       \
            2               5
        /       \               \
    3               4               6
                        \
                            5
                                \
                                    6

And move the root's left subtree over to the right.

Then, set root's left pointer to null.


                    1
                        \
                            2               
                        /       \               
                    3               4               
                                        \
                                            5
                                                \
                                                    6

Now, we move to root's right and repeat our process.

```

O(n) in time complexity and O(1) in space.

---

Python:

```python

class Solution:

    def flatten(self, root):

        if not root:
            return

        while root:
            
            # need to move over left subtree to right
            if root.left:
                
                # find rightmost to left subtree to save our root's right subtree
                rightMost = root.left
                while rightMost.right:
                    rightMost = rightMost.right
                rightMost.right = root.right

                # move over left subtree to right
                root.right = root.left
                root.left = None
            
            root = root.right
```
