# 109. Convert Sorted List to Binary Search Tree

Given the head of a singly linked list where elements are sorted in ascending
order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.

---

The question is similar to converting the given sorted array into a height
balanced BST. We can acertain that inorder traversal on the tree yields
a sorted list. Then, to build the height balanced tree, we choose the mid-value
as a root, and populate its left subtree to left of sorted order and vice
versa. Since we have a linked list, we would first need to traverse once to
determine the length to compute the mid point. At each recursive depth, we
traverse to left upto the mid way point. Then, create a node as a current head
of the list. Consume it, then move onto right.

Time complexity would be O(n) and this will require O(n) to build the tree.

---

Java:

```java

class Solution109 {

    private ListNode head;

    public TreeNode sortedListToBST(ListNode head)
    {
        this.head = head;
        int length = 0

        while (head != null)
        {
            head = head.next;
            length += 1;
        }

        return buildHelper(0, length - 1);
    }

    private TreeNode buildHelper(int l, int r)
    {
        if (l > r)
            return null;

        int m = l + (r - l) / 2;

        TreeNode leftNode = buildHelper(l, m - 1);
        TreeNode currNode = new TreeNode(this.head.val);

        this.head = this.head.next;

        currNode.left = leftNode;
        currNode.right = buildHelper(m + 1, r);
        
        return currNode;
    }
}

```
