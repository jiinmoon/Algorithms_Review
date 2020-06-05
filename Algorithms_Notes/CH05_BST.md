# Chpater 5: Binary Search Trees

BST is a binary tree which its elements are positioned such that all values in
the left subtree are less tha nvalues in the right subtree.

## Section 5.1: Binary Search Tree - Insertion

```Python

class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def insertBST(self, root, node):
    # insert node into the BST.
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if not root.left:
                root.left = node
            else:
                self.insert(root.left, node)
        else:
            if not root.right:
                root.right = node
            else:
                self.insert(root.right, node)

```

## Section 5.2: Binary Search Tree - Deletion

When deleting a node in BST, we have to consider three cases:

    1. Target node is the leaf node.
    2. Target node has a single child.
    3. Target node has both children.

In case 1, we can simply delete target node.

In case 2, we copy over the child's value, then delete the child.

In case 3, we need to find the minimum of right sub tree(or maximum of left
subtree) to copy over the value, and then delete the copied over value.

```Python

def deleteNode(self, root, data):
    # delete the node with data.
    if not root:
        return root
    # traverse to find the node with data.
    elif data < root.data:
        root.left = self.deleteNode(root.left, data)
    elif data > root.data:
        root.right = self.deleteNode(root.right, data)
    else:
        # case 1: leaf node.
        if not root.left and not root.right:
            root = None
        # case 2: single child.
        elif not root.left:
            root = root.right
        elif not root.right:
            root = root.left
        # case 3: both children.
        else:
            temp = root.right
            while temp.left:
                temp = temp.left
            root.data = temp.data
            root.right = deleteNode(root.right, temp.data)
    return root

```

## Section 5.3: LCA in a BST

```Python

def findLCA(self, root, p, q):
    if not root:
        return None

    if p.data == root.data or q.data == root.data:
        return root
    elif p.data <= root.data and q.data > root.data or \
        q.data <= root.data and p.data > root.data:
        return root
    elif root.data > max(p.data, q.data):
        return self.findLCA(root.left, p, q)
    else:
        return self.findLCA(root.right, p, q)

```



