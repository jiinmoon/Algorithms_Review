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

---

We may populate each of the next pointer in the same level using the BFS
algorithm as it traverses through the given tree depth-wise.

Time and space complexity would be O(n) as we need to visit each of the nodes.

---

Java:

```java

class Solution116 {

    public Node connect(Node root)
    {
        if (root == null)
            return null;

        Queue<Node> queue = new LinkedList<>(List.of(root));

        while (!queue.isEmpty())
        {
            int i = 0, level_size = queue.size();
            Node prevNode = null;

            while (i++ < level_size)
            {
                Node currNode = queue.poll(); 

                if (prevNode != null)
                    prevNode.next = currNode;

                prevNode = currNode;

                if (currNode.left != null)
                {
                    queue.offer(currNode.left);
                    queue.offer(currNode.right);
                }
            }
        }

        return root;
    }
}

```
