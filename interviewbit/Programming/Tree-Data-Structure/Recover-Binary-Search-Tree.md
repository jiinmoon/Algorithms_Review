# Recover Binary Search Tree

    Two elements of a binary search tree (BST) are swapped by mistake.
    Tell us the 2 values swapping which the tree will be restored.


Note:
    
    A solution using O(n) space is pretty straight forward. Could you devise
    a constant space solution? 

---

## Approach:

The naive solution would be to perform inorder traversal and build the ordered
list of elements to find the two out of place elements. This would take O(n) in
space. Another approach would be to maintain the previous node visited, and
compare as we iterate forward.

O(n) in time complexity to iterate the nodes once and O(1) in space.

---

Python: Iterative inorder approach.

```python

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, root):
        
        stack = []
        prev, swap1, swap2 = float('-inf'), None, None
        
        while root or stack:
            
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            
            if root.val <= prev:
                if not swap1:
                    swap1 = prev
                if swap1:
                    swap2 = root.val
            
            prev = root.val
            root = root.right
        
        return [swap2, swap1]

```

Java: Recursive inorder approach.

```java

/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) {
 *      val = x;
 *      left=null;
 *      right=null;
 *     }
 * }
 */
public class Solution {

    TreeNode prev, swapped1, swapped2;
    
    public ArrayList<Integer> recoverTree(TreeNode A) 
    {
        this.prev = new TreeNode(Integer.MIN_VALUE);
        this.swapped1 = null;
        this.swapped2 = null;
        
        inorder(A);

        ArrayList<Integer> result = new ArrayList<>();
        result.add(this.swapped2.val);
        result.add(this.swapped1.val);
        
        return result;
    }
    
    private void inorder(TreeNode node)
    {
        if (Objects.isNull(node))
            return;
        
        inorder(node.left);
        
        if (node.val <= this.prev.val)
        {
            if (Objects.isNull(this.swapped1))
                this.swapped1 = this.prev;
            if (Objects.nonNull(this.swapped1))
                this.swapped2 = node;
        }
        
        this.prev = node;
        
        inorder(node.right);
    }
}

```
