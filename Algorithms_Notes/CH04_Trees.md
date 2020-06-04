# Chpater 4: Trees

## Section 4.1: Typical anary tree representation

An anary tree (unlimited children per node) is usually represented as a binary
tree (two children per node). The 'next' child is regarded as a sibling.

## Section 4.2: Introduction

Trees are a subtype of the more general node-edge graph data structure.

    - It is acyclic.
    - It is connected. For any given node in the graph, every node is
    reacheable.

Trees are used in many data structures such as red-black trees, B-trees,
AB-trees, 23-trees, Heap and tries.

## Section 4.3: To check if two binary trees are same or not.

```Python

def isSameTree(self, p, q):
    if not p or not q:
        return p == q
    if p.val != q.val:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

```

