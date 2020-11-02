# 315 Count of Smaller Numbers After Self

Create a BST where left subtree is the nodes that are smaller than the current.
Hence, when we insert the new element, for each element that are smaller than
the node, we traverse left while counting. Record the count when finished
insertion.

Time complexity is O(n^2).

---

Python:

```python

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.lSum = 0

class Solution:
    def countSmaller(self, nums):
        if len(nums) < 2:
            return [0] * len(nums)

        res = [0] * len(nums)
        root = BSTNode(nums[-1])

        for i in range(len(nums)-2, -1, -1):
            curr = root
            lcount = 0

            # insertion into BST
            # count the times that we are moving to right + current lSum
            while True:
                if nums[i] < curr.val:
                    curr.lSum += 1
                    if not curr.left:
                        curr.left = BSTNode(nums[i])
                        break
                    else:
                        curr = curr.left

                else:
                    lcount += curr.lSum
                    if nums[i] > curr.val:
                        lcount += 1
                    if not curr.right:
                        curr.right = BSTNode(nums[i])
                        break
                    else:
                        curr = curr.right

            res[i] = lcount

        return res
```
