337 House Robber III
====================

The thief has found himself a new place for his thievery again. There is only
one entrance to this area, called the "root." Besides the root, each house has
one and only one parent house. After a tour, the smart thief realized that "all
houses in this place forms a binary tree". It will automatically contact the
police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without
alerting the police.

---

We recrusively traverse down the tree; starting from bottom, we return maximum
profit that can be made by robbing the current node or skipping the current
node. Since we have children, we need to compute for both cases.

At each node, maxProfit that can be made by robbing current node should be the
sum of current node value, left and right subtree's max profit that made by skipping left
and right. The maxProfit that can be made by skipping the current node should
be sum of maximum of either values returned from the children.

---

C++:

```cpp
class Solution {
public:
    int rob(TreeNode* root) 
    {
        vector<int> res = helper(node);
        return std::max(res[0], res[1]);
    }

    vector<int> helper(TreeNode* node)
    {
        if (node == nullptr) return { 0, 0 };
        vector<int> l = helper(node->left);
        vector<int> r = helper(node->right);
        int robCurr = node->val + l[1] + r[1];
        int noRobCurr = std::max(l[0], l[1]) + std::max(r[0], r[1]);
        return { robCurr, noRobCurr };
    }
};
```
