# 116. Populating Next Right Pointers in Each Node

You are given a perfect binary tree where all leaves are on the same level, and
every parent has two children. The binary tree has the following definition:

```
struct Node {
    int val;
    Node *left;
    Node *right;
    Node *next;
}
```

Populate each next pointer to point to its next right node. If there is
no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does
not count as extra space for this problem.

---

We can fix the pointers by performing a level-order traversal or BFS on the
given binary tree. As we are iterating level by level, at each depth, we would
have all the nodes for the depth in our queue which we can iterate and attach
previous node to next.

---

Python:

```python

class Solution116:

    def populateNextRight(self, root):

        if not root:
            return None

        queue = [root]

        while queue:

            temp, prev = [], None

            for node in queue:
                if prev:
                    prev.next = node
                prev = node
                # given tree is perfect binary tree
                if node.left:
                    temp.append(node.left)
                    temp.append(node.right)

            queue = temp

        return root
```
