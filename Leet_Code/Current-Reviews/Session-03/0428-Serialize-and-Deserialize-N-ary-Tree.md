428 Serialize and Deserialize N-ary Tree
========================================

Design an algorithm to serialize and deserailize an N-ary tree.

---

We will simply use the preorder traversal to serialize the tree - we add the
current value to the result, and recursivle visit all the child nodes of the
current node. To denote that each node's children are processed, we add in
a special character.

To restore this, we will reverse the process by taking the look at the given
data; until the data does not reach the special character that we embedded to
denote the end of children thus end of the child of the current node, we can
create a new children node to append to the current node. As well, since the
children can also have children, we recursively call on it self.

Time complexity should be O(n).

---

Python:

```python
class Codec:
    def serialize(self, root):
        def helper(node):
            if not node: return
            res.append(str(node.val))
            for nextNode in node.children:
                helper(nextNode)
            res.append("#")
        res = list()
        helper(root)
        return " ".join(res)

    def deserialize(self, data):
        def helper(node):
            if not data: return
            while data[-1] != "#":
                newNode = Node(int(data.pop()), list())
                node.children.append(newNode)
                helper(newNode)
            data.pop()
        data = data.split()[::-1]
        root = Node(int(data.pop()), list())
        helper(root)
        return root
```
