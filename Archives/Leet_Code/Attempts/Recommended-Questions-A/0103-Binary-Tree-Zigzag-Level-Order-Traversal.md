# 103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

---

We use BFS to grather up the nodes depth-wise. Then, for every depth, we flip
and reverse the order of the nodes found to create zigzag ordering. The time
complexity would be O(n) and the space complexity is O(n) as well to gather all
the nodes to return.

---

Java:

```java

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) return new LinkedList<>();

        boolean flip = false;
        List<List<Integer>> result = new LinkedList<>();
        List<TreeNode> queue = new LinkedList<>(List.of(root));

        while (!queue.isEmpty()) {
            List<Integer> currentDepth = new LinkedList<>();
            for (TreeNode node : queue) currentDepth.add(node.val);
            if (flip) Collections.reverse(currentDepth);
            flip = !flip;
            result.add(currentDepth);

            List<TreeNode> temp = new LinkedList<>();
            for (TreeNode node : queue) {
                if (node.left != null) temp.add(node.left);
                if (node.right != null temp.add(node.right);
            }
            queue = temp;
        }

        return result;
    }
}

```

Python:

```python

class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []

        flip = false
        result = []
        q = [root]

        while q:
            if flip:
                result.append([node.val for node in q[::-1])
            else:
                result.append([node.val for node in q])
            flip = not flip

            temp = []
            for node in q:
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            
            q = temp

        return result
```

