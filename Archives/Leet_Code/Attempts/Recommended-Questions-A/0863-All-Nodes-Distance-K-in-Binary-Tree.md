# 863. All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer
value K.

Return a list of the values of all nodes that have a distance K from the target
node.  The answer can be returned in any order.

---

To find the all nodes that are distance K away from the target node, we can
first traverse all the way down to the target node. From here, we can find the
simple K distanced nodes by traversing down to the target's children tree.
However, we also need to consider the nodes that potential distance K away
through the target node's parent and ancestor path. To resolve this, we check
to see where we have found the target node from the parent. And depending on
where we have found the target node from the parent node, we can decide to look
for other nodes distance K away that is on the other side of the subtree where
target node exists.

---

Java:

```java

class Solution {
    
    public List<Integer> allNodesDistK(TreeNode root, TreeNode target, int K) {
        List<Integer> result = new LinkedList<>();
        searchAll(root, target, K, result);
        return result;
    }

    public void searchDown(TreeNode curr, int d, result) {
        if (curr == null) return;
        if (d == 0) result.add(curr.val);
        else {
            searchDown(curr.left, d - 1, result);
            searchDown(curr.right, d - 1, result);
        }
    }
    
    public int searchAll(TreeNode curr, TreeNode target, int K, List<Integer> result) {
        if (curr == null) return -1;
        if (curr.val == target.val) {
            searchDown(curr, K, result);
            return 0;
        }

        int left = searchAll(curr.left, target, K, result);
        int right = searchAll(curr.right, target, K, result);

        if (left == -1 && right == -1) return -1;

        int dist = Math.max(left, right) + 1;

        if (K - dist == 0) result.add(curr.val);
        else if (K - dist > 0) {
            TreeNode otherSide = (left == -1) ? curr.left : curr.right;
            searchDown(otherSide, K - dist - 1);
        }

        return K - dist;
    }

}

```

Python:

```python

class Solution:
    def allNodesDistK(self, root, target, k):
        def searchDown(node, dist):
            if not node: return
            if not dist:
                result.append(node.val)
                return
            searchDown(node.left, dist - 1)
            searchDown(node.right, dist - 1)

        def searchAll(node):
            if not node:
                return -1
            if node == target:
                searchDown(node, k)
                return 0
            # indicator of where the target node has been found
            l, r = searchAll(node.left), searchAll(node.right)
            dist = k - (max(l, r) + 1)
            if not dist:
                searchDown(node, 0)
            elif dist > 0:
                otherSide = node.left if l == -1 else node.right
                searchDown(otherSide, dist - 1)
            return k - dist
        
        result = list()
        searchAll(root)
        return result
```
