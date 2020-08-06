108 Covert Sorted Array to Binary Search Tree
=============================================

Question:
---------

Given an array where elements are sorted in ascending order, convert it to
a height balanced BST.

Solutions:
----------

The hint is with the ehgith balanced BST. To generate such BST, it left and
right subtree has to be balanced - meaning that at each depth, we need to
choose "mid" value that divides the array cleanly into two halves that will
populate left and right subtrees.

Codes:
------

Python:

```python
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        node = ListNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
```

---

**Source:**

LeetCode: [Convert-Sorted-Array-to-Binary-Search-Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree)
