# Kth Smallest Element In Tree

    Given a binary search tree, write a function to find the kth smallest element
    in the tree.

---

## Approach:

The nature of the BST is such that _inorder_ traversal on the tree will give us
sorted list of elements in ascending order. Hence, naive solution would be to
first itearte entire tree in inorder fashion, and then find the Kth element. To
collect the values this way would cost us O(n) in space complexity.

Another way would be to iterate on the given tree; traverse to the leftmost
node, and then iterate forward K steps. We can use recursion or iteratively
with stack. This may improve the space complexity slightly due to not having to
iterate on the entire tree. But the space complexity is still bounded by O(n)
as in worst case, we have a linked list.

In terms of time complexity, it would be O(n) as we may have to iterate on
a linked list.

---

## Solution:

Java: Iterative approach.

```java

/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    
    public int kthsmallest(TreeNode root, int k) 
    {
        Stack<TreeNode> stack = new Stack<>();

        // traverse to leftmost node
        for (;  Objects.nonNull(root); 
                stack.push(root), 
                root = root.left);
        
        while (!stack.isEmpty())
        {
            root = stack.pop();
            
            // traversed k steps forward
            if (--k == 0)
                return root.val;
            
            // otherwise, move forward
            if (Objects.nonNull(root.right))
            {
                root = root.right;
                for (;  Objects.nonNull(root);
                        stack.push(root),
                        root = root.left);
            }
        }
        return -1;
    }
}

```

C++: recursive approach.

```cpp

void inorder(TreeNode* A, int &B, int &result)
{
    if (A != NULL)
    {
        inorder(A->left, B, result);

        if (--B == 0)
            result = A->val;

        inorder(A->right, B, result);
    }
}

int Solution::kthsmallest(TreeNode* A, int B) 
{
    int result;
    inorder(A, B, result);

    return result;
}
```
