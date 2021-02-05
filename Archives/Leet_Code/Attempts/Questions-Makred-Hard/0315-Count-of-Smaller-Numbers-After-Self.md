# 315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller
elements to the right of nums[i].

---

Naive approach would be to start from the end of the list and iterate inwards.
At each index, we scan to left to find the number of elements which are smaller
than itself. This is O(n^2) in time complexity.

There is another method that can potentially improve the time complexity
logrithmically in best and average case which is using the Binary Search Tree.
By modifying each node to maintain the count of total number of nodes on its
left subtree, we can potentially find the result in O(n * log(n)) as insertion
on the binary search tree is logrithmic process. However, at worst case we may
have a linked list which still brings our time complexity to O(n^2).

The idea is to starting from the end, treat the right most value as a root of
this binary search tree. Then for each node encountered, we move downward
maintain the left subtree counts.

---

Python:

```python

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.smaller = 0

class Solution:
    def countOfSmaller(self, nums):
        if not nums:
            return []

        m = len(nums)
        result = [0] * m
        root = TreeNode(nums[-1])

        for i in range(m-2, -1, -1):
            curr = root
            count = 0

            while True:
                # insert to left subtree
                if nums[i] < curr.val:
                    curr.smaller += 1
                    if not curr.left:
                        curr.left = TreeNode(nums[i])
                        break
                    else:
                        curr = curr.left
                # insert to right subtree
                else:
                    count += curr.smaller
                    if nums[i] > curr.val:
                        count += 1 # include current as well
                    if not curr.right:
                        curr.right = TreeNode(nums[i])
                        break
                    else:
                        curr = curr.right

            result[i] = count

        return result
```
