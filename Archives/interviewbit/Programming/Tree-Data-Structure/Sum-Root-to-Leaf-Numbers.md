# Sum Root to Leaf Numbers

    Given a binary tree containing digits from 0-9 only, each root-to-leaf path
    could represent a number.

    An example is the root-to-leaf path 1->2->3 which represents the number 123.

    Find the total sum of all root-to-leaf numbers % 1003.

---

## Approach:

Recursively traverse down to the leaf nodes whilst building the path sum down.
Once we have reached the leaf, we add path sum to our result.

O(n) in time complexity.

---

Java:

```java

public class Solution {
    
    int result;
    
    public int sumNumbers(TreeNode A) 
    {   
        helper(A, 0);
        return result % 1003;
    }
    
    private void helper(TreeNode node, int pathSum)
    {
        if (Objects.isNull(node))
            return;
        
        pathSum = (pathSum * 10 + node.val) % 1003;
        
        if (Objects.isNull(node.left) && Objects.isNull(node.right)) {
            this.result += pathSum;
        } else {
            helper(node.left, pathSum);
            helper(node.right, pathSum);
        }
    }
}

```
