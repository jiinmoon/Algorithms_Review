# 1120. Maximum Average Subtree

Given the root of a binary tree, find the maximum average value of any subtree
of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The
average value of a tree is the sum of its values, divided by the number of
nodes.)

---

To find the max average of any subtree, we first traverse all the way down to
the bottom of the tree. As we recursively move up to given tree, we return the
count of the nodes we have seen as well as the sum of the all the node values.
By using these, we can compute the average value at every subtree starting from
each of the node. Time complexity would be O(n) and space complexity is O(n).

---

Java:

```java

class Solution {
    
    static class Pair {
        int count, sum;

        public Pair(int count, int sum) {
            this.count = count;
            this.sum = sum;
        }
    }

    double result = 0;
    
    public double maximumAverageSubtree(TreeNode root) {
        helper(root);
        return this.result;
    }

    public Pair helper(TreeNode node) {
        if (node == null) return new Pair(0, 0);
        Pair lPair = helper(node.left);
        Pair rPair = helper(node.right);
        int currCount = 1 + lPair.count + rPair.count;
        int currSum = node.val + lPair.sum + rPair.sum;
        this.result = Math.max(this.result, (double) currSum / currCount);
        return new Pair(currCount, currSum);
    }
}


```


Python:

```python

class Solution:
    def maxAverageSubtree(self, root):
        def helper(node):
            if not node:
                return 0, 0
            lCount, lSum = helper(node.left)
            rCount, rSum = helper(node.right)
            currCount = 1 + lCount + rCount
            currSum = node.val + lSum + rSum
            self.maxAvg = max(self.maxAvg, currSum / currCount)
            return currCount, currSum
        self.maxAvg = 0
        helper(root)
        return self.maxAvg
```
