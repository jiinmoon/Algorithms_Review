# 1328. Balance a Binary Search Tree

Given a binary search tree, return a balanced binary search tree with the same
node values.

A binary search tree is balanced if and only if the depth of the two subtrees
of every node never differ by more than 1.

If there is more than one answer, return any of them.

---

Simplest approach would be to retrieve the sorted list of elements present in
the BST via inorder traversal; and then build a new tree that is
height-balanced by repeatedly take the mid-point as a new root of subtree.

O(n) in time and space for collecting inordered nodes; then build.

---

Java:

```java

class Solution1328 {

    List<TreeNode> sorted;

    public TreeNode balanceBST(TreeNode root)
    {
        if (root == null)
            return null;

        this.sorted = new ArrayList<>();
        inorder(root);

        return build(0, this.sorted.size()-1);
    }

    private void inorder(TreeNode node)
    {
        if (node != null)
        {
            inorder(node.left);
            this.sorted.add(node);
            inorder(node.right);
        }
    }

    private TreeNode build(int start, int end)
    {
        if (start > end)
            return null;
        
        int mid = start + (end - start) / 2;

        TreeNode curr = this.sorted.get(mid);
        curr.left = build(start, mid - 1);
        curr.right = build(mid + 1, end);

        return curr;
    }
}

```
