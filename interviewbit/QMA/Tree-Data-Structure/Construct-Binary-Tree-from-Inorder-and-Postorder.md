# Construct Binary Tree from Inorder and Postorder

Given inorder and postorder traversal of a tree, construct the binary tree.

---

Similar to preorder approach, we traverse in postorder fashion; root will be
the top of the postorder and the range of the inorder will give us how to
populate to left and right childs.

O(n) in time complexity.

---

Java:

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

    ArrayList<Integer> inorder;
    ArrayList<Integer> postorder;
    
    public TreeNode buildTree(ArrayList<Integer> A, ArrayList<Integer> B) 
    {
        this.inorder = A;
        this.postorder = B;
        return build(0, A.size() - 1);
    }
    
    private TreeNode build(int l, int r)
    {
        if (l > r)
            return null;

        TreeNode node = new TreeNode(this.postorder.remove(this.postorder.size() - 1));

        if (l == r)
            return node;

        int idx = this.inorder.indexOf(node.val);
        node.right = build(idx + 1, r);
        node.left = build(l, idx - 1);

        return node;
    }
}

```
