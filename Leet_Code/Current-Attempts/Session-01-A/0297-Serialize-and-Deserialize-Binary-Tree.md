# 297 Serialize and Deserialize Binary Tree

Simply, perform preorder traversal while recording the node values. Restoring
process is the reverse of that.

---

Python:

```python

class Solution:
    def serialize(self, root):
        def helper(node):
            if not node:
                res.append("Null"))
                return
            res.append(str(node.val))
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)
        
        res = list()
        helper(root)
        return ",".join(res)

    def deserialize(self, data):
        def helper():
            if not data:
                return
            curr = data.pop()
            if curr == "Null":
                return
            node = Node(curr)
            node.left = helper()
            node.right = helper()
            return node
            
        data = data.split(",")[::-1]
        return helper()
```
