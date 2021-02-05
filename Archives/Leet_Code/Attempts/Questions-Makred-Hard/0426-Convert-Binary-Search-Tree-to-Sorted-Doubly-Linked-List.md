# 426. Convert Binary Search Tree to Sorted Doubly Linked List

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor
and successor pointers in a doubly-linked list. For a circular doubly linked
list, the predecessor of the first element is the last element, and the
successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left
pointer of the tree node should point to its predecessor, and the right pointer
should point to its successor. You should return the pointer to the smallest
element of the linked list.

---

Naive approach would be to gather all the nodes in a list using inorder
traversal, and then iterate on this list to create the doubly linked list.
However, we want to perform this process in-place, thus we seek to perform this
operation while traversing.

From bottom up, we determine the head of the left and right subtrees. At each
node, the returned values from the left and right subtrees should be of their
respective sorted doubly linked list. The problem is the we need to tie the
left subtree list to the right subtree list. To do so, we create the lists at
each node in such fashion that makes a circular doubly linked list.

At each node, left subtree list head's right pointer should be fixed back to
the current node. As well, last left subtree list tail should point back to the
current to close the circle.

Also, for right subtree, similar operations follow; current node is the new
head of the right subtree list. But we also need to mark the right subtree list
tail (left of returned right head), as we need to close the circle between left
and right after adding current node.

The time complexity should be O(n).

---

Python:

```python

class Solution:
    def convert(self, root):
        if not root: return None

        leftListHead = self.convert(root.left)
        rightListHead = self.convert(root.right)

        # attach current node as last in left list
        if leftListHead:
            root.left = leftListHead.left
            # make it circular
            leftListHead.left.right = root
        else:
            # otherwise, current is the beginning of new left list
            leftListHead = root
        
        # attach current node as first in right list
        if rightListHead:
            root.right = rightListHead
            # save rightListTail to tie left and right list later
            rightListTail = rightListHead.left
            rightListHead.left = root
        else:
            # otherwise, current is the beginning of new right list
            rightListHead = root

        # tie left and right list; making it circular
        leftListHead.left = rightListTail
        rightListTail.right = leftListHead

        return leftListHead
```



