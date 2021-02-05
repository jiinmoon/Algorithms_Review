# 1315. Sum of Nodes with Even Valued Grandparent

Given a binary tree, return the sum of values of nodes with even-valued
grandparent.  (A grandparent of a node is the parent of its parent, if it
exists.)

If there are no nodes with an even-valued grandparent, return 0.

---

We can compute the sum of nodes that have even valued grandparent by simply
recursively traverse on the tree while maintaining the value of the parent and
grandparent;

At each node, we check to see that grandparent value of even; if so, then we
add our current node value to our sum to be returned from left and right
subtree.

For example:

```
Tree = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]

helper(TreeNode node, int parentValue, int grandParentValue)

helper(6, 1, 1):
    l =     helper(7, 6, 1)     = 9
    r =     helper(8, 6, 1)     = 9
    is a root; return 9 + 9 = 18

(left of root)

-> helper(7, 6, 1):
    l =     helper(2, 7, 6)     = 2
    r =     helper(7, 7, 2)     = 7
    grandparent of 1 is not even; return 2 + 7 = 9

-> helper(2, 7, 6):
    l =     helper(9, 2, 7)     = 0
    r =     0
    grandparent of 6 is even; return 0 + 0 + 2 = 2

-> helper(9, 2, 7):
    l =     0
    r =     0
    grandparent of 7 is not even; return 0 + 0 = 0

-> helper(7, 7, 2):
    l =     helper(1, 7, 7)     = 0
    r =     helper(4, 7, 7)     = 0
    grandparent of 2 is even; return 0 + 0 + 7 = 7

(right of root)

-> helper(8, 6, 1):
    l =     helper(1, 8, 6)     = 1
    r =     helper(3, 8, 6)     = 8
    grandparent of 1 is not even; return 1 + 8 = 9

-> helper(1, 8, 6)
    l =     0
    r =     0
    grandparent of 6 is even; return 0 + 0 + 1 = 1

-> helper(3, 8, 6)
    l =     0
    r =     helper(5, 3, 8)     = 5
    grandparent of 6 is even; return 0 + 5 + 3 = 8

```

Time complexity would be typical linear.

---

Java:

```java

class Solution1315 {

    public int sumEvenGranparent(TreeNode root)
    {
        return (root == null) ? 0 : helper(root, 1, 1);
    }

    private int helper(TreeNode node, int parentVal, int grandVal)
    {
        if (node == null)
            return 0;

        int currSum = helper(node.left, node.val, parentVal) + helper(node.right, node.val, parentVal);

        // add current to on-going sum iff grandparent was even
        return (grandVal % 2 == 0) ? currSum + node.val : currSum;
    }
}

```
