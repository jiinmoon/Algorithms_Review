951 Flip Equivalent Binary Trees
================================

For a binary tree T, we can define a flip operation as follows: choose any
node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can
make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two
trees are flip equivelent or false otherwise.

---

We simply recursively traverse down the trees, checking for whether the two
tree's nodes are equal to each other or not. Then, we visit the next depth in
two cases: non-flip and lip.

Time complexity still remains O(n) since we are simply visiting the node in
different way (equivalent to performing two iteration).

---

C++:

```cpp
class Solution {
public:
    bool flipEquiv(TreeNode* p, TreeNode* q)
    {
        if (p == nullptr || q == nullptr)
            return p == q;
        if (p->val != q->val)
            return false;
        return (flipEquiv(p->left, q->left) && flipEquiv(p->right, q->right)) ||
                (flipEquiv(p->left, q->right) && flipEquiv(p->right, q->left));
    }
};
```
