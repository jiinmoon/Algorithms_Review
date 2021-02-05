""" 4.12 Paths With Sum


Question:

    You are given a binary tree in which each node contains an integer value
    (which might be positive or negative). Design an algorithm to count the
    number of paths that sum to a given value. The path does not need to start
    or end at the root or a leaf, but it must go downwards (traveling only from
    parent nodes to child nodes).

---

This is finding paths problem where for each nodes that we visit, we consider
continuing down the paths while computing the path sum. If we can find the sum,
then we found the path.

Above approach is the brute force approach where we traverse to each node and at
each node we recursivelu try all paths downwards, tracking the sum. However,
this runtime is O(n lg n) in balanced tree; and O(n^2) in unbalanced tree.

The optimized case utilizes the fact that we repeatedly go over some of the
paths over an over again. Suppose we have a path, then this problem becomes how
many contiguous subsequences in this array sum to a target sum?

Suppose we have chosen the DFS to visit each of the nodes, then pseudocode is as
follows:

1. track its runningSum. increment is by node.val

2. look up runningSum - targetSum in hashTable. the value indicates total. set
totalPaths to this value.

3. if runningSum == targetSum, then there's one additional path that starts at
the root. increment totalPaths.

4. add runningSum to the hash table (incrementing the value if it's already
there).

5. recurse left and right, counting the number of paths with sum targetSum.

After we are finished, decrement the value of runningSum in the Hash table.

"""
