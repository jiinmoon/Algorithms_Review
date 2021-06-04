# 109. Convert Sorted List to Binary Search Tree

Given the head of a singly linked list where elements are sorted in ascending
order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.

---

Similar to the previous problem where we have to convert the given sorted array
of integer into the height balanced BST, we borrow the similar approach. That
is, we continue to choose the mid element from the sorted list to be our
current node and build our binary search tree recursively to its left and
right.

To do so, we first need to measure the length of the linked list so that we can
compute the mid point at each depth of our recursion. By computing the left and
right pointers, we can find current mid point.

If we build it in preorder fashion, we would first traverse all the way to the
left of our BST. Then, set the current node value as the head of our given
linked list and move forward.

---

Python:

```python

class Solution109:

    def convertListToBST(self, head):

        # compute length of given linked list

        length, runner = 0, head
        while runner:
            length += 1
            runner = runner.next

        def buildBST(l, r):
            nonlocal head

            if l > r:
                return None

            m = l + (r - l) // 2
            leftChild = buildBST(l, m - 1)
            currNode = TreeNode(head.val)
            # consume current node
            head = head.next
            currNode.left = leftChild
            currNode.right = buildBST(m + 1, r)

            return currNode

        return buildBST(0, length - 1)
```


