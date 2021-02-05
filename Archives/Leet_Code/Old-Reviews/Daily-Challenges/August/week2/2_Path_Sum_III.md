# LeetCode Daily Challenge: August Week.2 - Day.1

## Question

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go
downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range
-1,000,000 to 1,000,000.

## Solution

What makes the question difficult is that the path does not have to start at
root nor end at leaf. If we are to approach this naively, we would be
performing tree traversal on each of the nodes.

Instead, we will use a hashmap to record the count of paths from root to
current node. Iterate on the tree to visit each nodes and at each node, we
record the number of paths that end there with target sum.

Go:

```
func pathSum(root *TreeNode, sum int) int {
    paths := map[int]int{0 : 1}
    return traverse(root, sum, 0, paths)
}

func traverse(node *TreeNode, sum, partial int, paths map[int]int) int {
    if node == nil {
        return 0
    }

    partial += node.Val
    count = paths[partial - sum]

    paths[partial] += 1
    count += traverse(node.Left, sum, partial, paths)
    count += traverse(node.Right, sum, partial, paths)
    paths[partial] -= 1
    return count
}
```

