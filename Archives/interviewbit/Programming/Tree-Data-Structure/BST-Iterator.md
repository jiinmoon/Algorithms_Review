# BST Iterator


    Implement an iterator over a binary search tree (BST). Your iterator will be
    initialized with the root node of a BST.

    The first call to next() will return the smallest number in BST. Calling next()
    again will return the next smallest number in the BST, and so on.


    Note: next() and hasNext() should run in average O(1) time and uses O(h)
    memory, where h is the height of the tree.

    Try to optimize the additional space complexity apart from the amortized time
    complexity. 

## Approach:

We can implement the Iterator using the stack data structure. During
initialization (or construction), we spend O(n) time to save the nodes unto the
stack, reaching the left most node to find the smallest number in BST.

When next() is called, top of the stack will be the next node to be returned;
but we should also take care that all the subtrees below the node's to right
child must also be included in the stack as well. Hence, this also will be O(n)
in worst case scenario where the BST is a linked list. On average, the height
balanced BST will be O(log(n)).

---

Java:

```java

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class Solution {
    
    private Stack<TreeNode> stack;
    
    public Solution(TreeNode root) 
    {
        this.stack = new Stack<>();
        for (;  Objects.nonNull(root);
                this.stack.push(root), 
                root = root.left);
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() { return !this.stack.isEmpty(); }

    /** @return the next smallest number */
    public int next() 
    {
        if (!hasNext())
            return -1;
        
        TreeNode node = this.stack.pop();
        
        if (Objects.nonNull(node.right))
        {
            TreeNode temp = node.right;
            for (;  Objects.nonNull(temp);
                    this.stack.push(temp),
                    temp = temp.left);
        }
        
        return node.val;
    }
}

/**
 * Your Solution will be called like this:
 * Solution i = new Solution(root);
 * while (i.hasNext()) System.out.print(i.next());
 */
```
