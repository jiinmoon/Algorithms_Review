""" 4.9 BST Sequences


Question:

    A BST was created by traversing through an array from left to right and
    inserting each element. Given a BST with distinct elements, print all
    possible arrays that could have led to this tree.

---

Always start with a good example to fully grasp the concept before jumping into
the question such as this.

First, we notice that the BST was created by inserting the values of array from
left to right; this means that we are absolutely sure that the root value must
be the very first element in the array.

Once we have a root value, we know that in BST, the values less than root will
be in left subtree and greater than will be in right subtree. Then, we
understand that the ordering does not appear to matter. For example, if we have
a root node 5, and value 1 and 7 on left and right. Then the original array
could have been 5 1 7 or 5 7 1.

This applies recursively down to any particular node and its subtrees. The
possible answers appears to be 'weaved' choices of where they appear to be.

"""
