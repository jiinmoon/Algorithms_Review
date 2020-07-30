109 Convert Sorted List to Binary Search Tree
=============================================

Question:
---------

Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.

Solutions:
----------

The same approach as problem 108 can be used here. Only difference is that now
we need to iterate to find the mid node to split the linked list into two lists
of equal lengths.

Codes:
------

Python:

```python
class Solution:
    def sortedLinkedListToBST(self, head):
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        # we want slow to be prev to the mid node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fsat.next.next
    
        head2 i= slow.next
        slow.next = None # split the list into two halves

        curr = TreeNode(head2.val)
        curr.left = self.sortedLinkedListToBST(head)
        curr.right = self.sortedLinkedListToBST(head2.next)
        return curr
```

---

**Source:**

LeetCode: [Convert-Sorted-List-to-Binary-Search-Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree)
