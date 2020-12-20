# Min Depth of Binary Tree

    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the root
    node down to the nearest leaf node.

---

## Approach:

Naively approaching this problem, it first appears to be inverse of maximum
depth or height problem. However, we quickly run into the problem when we
mindlessly try to return the minimum of the left and right subtree at each
depth. It could be that a node may only have a single child - along these
singlular paths, we should return the maximum instead of the minimum.

O(n) in time complexity.

---

Java:

```java

public class Solution {

    public int minDepth(TreeNode A) 
    {
        if (Objects.isNull(A))
            return 0;
        
        if (Objects.isNull(A.left) && Objects.isNull(A.right))
            return 1;
            
        int l = minDepth(A.left), r = minDepth(A.right);
        
        return (l == 0 || r == 0) ? Math.max(l, r) + 1 : Math.min(l, r) + 1;
    }
}

```
