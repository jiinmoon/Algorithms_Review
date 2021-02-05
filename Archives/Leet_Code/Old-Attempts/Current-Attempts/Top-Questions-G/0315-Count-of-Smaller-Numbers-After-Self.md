# 315 Count of Smaller numbres After Self

You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller
elements to the right of nums[i].

---

Naive approach would be to for each element, iterate to right to count the
elements which are smaller than the current element - which is O(n^2) in time
complexity.

To improve upon this, we use Binary Search Tree and leaverage on its design
that all nodes to left subtree should contain elements less than the parent's;
and vice versa. So, this would be iterating on the given array, and inserting
the values onto the BST while maintaining at each no the count of the nodes to
its left. Since insertion into BST consts O(log(n)), the total time complexity
should be O(n * log(n)).

---

Python:

```python

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        self.lCount = 0

class Solution:
    def countSmaller(self, nums):
        counts = [0] * len(nums)
        if len(nums) < 2:
            return counts

        rootNode = TreeNode(nums[-1])
       
        # iterate from right to left; insert nums
        # right to left since we want to increase the counts
        for i in range(len(nums)-2, -1, -1):
            currNode = rootNode
            count = 0

            while True:
                # if insertion value is less than the parent's value
                # it is to be inserted to left subtree; increase current parent
                # node's left node counts and advace or create
                if nums[i] < currNode.val:
                    curr.lCount += 1
                    if not currNode.left:
                        currNode.left = TreeNode(nums[i])
                        break
                    else:
                        currNode = currNode.left
                # if the insertion value is greater than parent's value
                # we move onto right subtree; we increase current count by
                # current parent's lcount to carry over the all left node
                # counts from the left subtree
                else:
                    count += currNode.lCount
                    if nums[i] > currNode.val:
                        count += 1
                    if not currNode.right:
                        currNode.right = TreeNode(nums[i])
                        break
                    else:
                        currNode = currNode.right
                
            # record the count for current value after finished insertion
            counts[i] = count
        
        return counts
```
