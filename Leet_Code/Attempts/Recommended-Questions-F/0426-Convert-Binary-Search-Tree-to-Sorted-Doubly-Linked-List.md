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

BST has a characteristic where inorder traversal on this data structure will
result us in ordered, sorted list of nodes. Thus, we could do this while
performing inorder, maintaining the prev and next nodes.

Other recursive method is to recursively we traverse down to left and right
- to the bottom of the left and right subtree. As we coming up, we fix the left
  subtree and right subtree. Time complexity should be O(n) in both cases.

In this process, we recursively move down to the bottom of the left and right
subtree. Starting from theses, we attempt to create a circular doubly linked
list. At each node, we try to make it such that returned node would be the
leftmost node from the currently sorted order of the tree. By making each node
circular, we only have to operate on the two nodes to at each step to expand
the linked list.

---

Python:

```python

class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return None

        # traverse down to bottom of left and right subtrees
        leftHead = self.treeToDoublyList(root.left)
        rightHead = self.treeToDoublyList(root.right)

        # as we come up, fix the pointers

        # if left subtree exists, current node value is greater than it
        # thus, in sorted order, returnd left node is to left of current node
        # it is also a doubly linked list, fix the right pointer of left
        if leftHead:
            root.left = leftHead.left
            leftHead.left.right = root
        # if it does not exist, current is the leftmost sorted node
        else:
            leftHead = root

        # likewise for right node returned from right subtree
        if rightHead:
            root.right = rightHead
            rightTail = rightHead.left
            rightHead.left = root
        else:
            rightTail = root
        
        # close the circle
        leftHead.left = rightTail
        rightTail.right = leftHead

        return leftHead
```


