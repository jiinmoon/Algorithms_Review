# 2-Sum Binary Tree

Given a binary search tree T, where each node contains a positive integer, and
an integer K, you have to find whether or not there exist two different nodes
A and B such that A.value + B.value = K.

Return 1 to denote that two such nodes exist. Return 0, otherwise.

---

### (1) Set.

Use set to record each of the values; while traversing if we can find the
target value in the set, we have 2 nodes sum to target. Uses O(n) in space.

### (2) Iterate from left and right.

Since we have a binary search tree, leftmost and rightmost values are
respectively minimum and maximum of the tree. Thus, we can use two pointers to
find the sum. If the current sum of two values at either end of the nodes are
less than target, we increment the smaller; and vice versa. O(h) in space
complexity since our stack does not have to maintain the entire nodes.

---

Python: Set.

```python

class Solution:

    def twoSumBinaryTree(self, root, target):

        def traverse(node):

            nonlocal seen

            if not node:
                return 0
            if target - node.val in seen:
                return 1
            seen.add(node.val)

            return traverse(node.left) or traverse(node.right)

        seen = set()

        return traverse(root)

```

Python: Two-Pointers.

```python

class Solution:

    def twoSumBinaryTree(self, root, target):

        stack1, stack2 = [], []
        curr1, curr2 = root, root

        while (curr1 or stack1) and (curr2 or stack2):

            while curr1:
                stack1.append(curr1)
                curr1 = curr1.left

            while curr2:
                stack2.append(curr2)
                curr2 = curr2.right

            temp1, temp2 = stack1[-1], stack2[-1]
            
            # cannot find; crossed mid point
            if temp1.val >= temp2.val:
                break
            
            currSum = temp1.val + temp2.val
            if currSum == target:
                return 1

            if currSum < target:
                curr1 = temp1.right
                stack1.pop()

            if currSum > target:
                curr2 = temp2.left
                stack2.pop()

        return 0
```

