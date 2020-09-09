1110 Delete Nodes And Return Forest
===================================

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to\_delete, we are left with a forest
(a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the
result in any order.

---

We recurisvely traverse down on the tree; if the node is not marked for delete
and also does not have a parent, we can add it to the result. Then, we
recursively build current node's left and right. We can complete this traversal
in O(n).

---

C++:

```cpp
class Solution
{
public:
    TreeNode* helper(TreeNode* node, bool hasParent, vector<TreeNode*> &res, unordered_set<int>& toDelete)
    {
        if (node == nullptr) return nullptr;
        // use `contains(const Key& key)` in C++20
        bool isDelete = toDelete.find(node->val) != toDelete.end();
        if (!hasParent && !isDelete)
            res.append(node);
        node->left = helper(node->left, !isDelete, res, toDelete);
        node->right = helper(node->right, !isDelete, res, toDelete);
        return (isDelete) ? nullptr : node;
    }

    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete)
    {
        vector<TreeNode*> res;
        unordered_set<int> toDelete;
        for (auto val : to_delete)
            toDelete.insert(val);
        helper(root, False, res, toDelete);
        return res;
    }
};

```

Python:

```python
class Solution:
    def delNodes(self, root, to_delete):
        def helper(node, hasParent):
            if not node: return
            delete = node.val in to_delete
            if not hasParent and not delete:
                res.append(node)
            # prev was marked for deletion?
            # children should have no parent
            node.left = helper(node.left, not delete)
            node.right = helper(node.right, not delete)
            return node if not delete else None

        res = list()
        to_delete = set(to_delete)
        
        helper(root, False)
        return res
```

