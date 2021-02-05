# 199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return
the values of the nodes you can see ordered from top to bottom.

---

Simple approach would be to perform BFS on the given binary tree - as we are
traversing depth by depth, at each depth, we can find the rightmost element
from the depth and add to our result. The time complexity should be O(n).

---

Java:

```java

class Solution {

    public List<Integer> rightSideView(TreeNode root) {
        if (root == null) return new LinkedList<>();

        Deque<TreeNode> queue = new LinkedList<>(List.of(root));
        List<Ineger> result = new LinkedList<>();

        while (!queue.isEmpty()) {
            Deque<TreeNode> temp = new LinkedList<>();
            result.add(queue.peekLast().val);

            while (!queue.isEmpty()) {
                TreeNode curr = queue.removeFirst();
                if (curr.left != null) temp.add(curr.left);
                if (curr.right != null) temp.add(curr.right);
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
    def rightSideView(self, root):
        if not root:
            return []

        q = [root]
        result = list()
        while q:
            result.append(q[-1].val)
            temp = list()
            for node in q:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp
        return result
```
