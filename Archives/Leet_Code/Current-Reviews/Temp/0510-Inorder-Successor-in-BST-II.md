# 510. Inorder Successor in BST II

Given a node in a binary search tree, find the in-order successor of that node
in the BST.

If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than
node.val.

You will have direct access to the node but not to the root of the tree. Each
node will have a reference to its parent node. Below is the definition for
Node:

```
class Node {
    public int val;
    public Node left;

    public Node right;
    public Node parent;
}
```
 

Follow up:

Could you solve it without looking up any of the node's values?

---

#### (1) Naively collecting inordered list.

To find next right successor of target; first node that is greater than target
or next right node in inordered sorted list, we can first traverse on entire
tree in inorder traversal then find the target value and return its next
neighbour. This would be O(n) in time complexity and space.

#### (2) Recursive searching.

Intuitively, the next greater value has to be in the right subtree (leftmost
value in the right subtree) or next greater value in the parents. So, as we
have a pointer to parent, we can split this into two cases:

1. Inorder successor is below the target node.

If such is that case, then it is the left-most node (smallest value) to its
right subtree.

2. Inorder successor is above the target node.

Then, we need to traverse upto the parents so long as we are coming from the
"right" subtree of the parent which denotes that the parent values are smaller.

---

Python: Recursive searching.

```python

class Solution510:

    def inorderSuccessor(self, node, target):
        
        # can search down
        if node.right:
            
            node = node.right
            while node.left:
                node = node.left
            return node

        else:
            
            # so long as we can move to smaler parents, do so
            while node.parent and node == node.parent.right:
                node = node.parent
            # return first parent that value is greater than target
            return node.parent
```

