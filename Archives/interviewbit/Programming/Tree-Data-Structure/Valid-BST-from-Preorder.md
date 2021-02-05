# Valid BST from Preorder

- Problem Description


    You are given a preorder traversal A, of a Binary Search Tree.
    Find if it is a valid preorder traversal of a BST.

- Problem Constraints


    1 <= A[i] <= 106
    1 <= |A| <= 105

- Input Format


    First and only argument is an integer array A denoting the pre-order traversal.

- Output Format


    Return an integer:

    0 : Impossible preorder traversal of a BST
    1 : Possible preorder traversal of a BST


## Approach:

Let's take a look at an example of a valid preorder of a BST:

                5
            /       \
        3               9
                    /       \
                    7       10

Preorder on a given BST will be [5, 3, 9, 7, 10].

For every root value chosen, the next greater value appearing on the preorder
list will be its first right hand child. For example, for root of 5, 9 is the
next right hand child; for root of 9, 10 would be next.

Then, following must hold: for every greater value we examine after another,
all the values previous has to be less than the next greater value (which is
found to be on the left subtree) and values after should be greater than it.

To check for this condition, we can use stack; for every value we see, if it is
found to be smaller than our current root value, it cannot be a valid preorder
of BST. We update the root by using stack; so long as the value we encountered
are greater than the top of our stack, we pop (removing the left subtree
values) while updating our root as the next greater value.

O(n) in time complexity and in space complexity.


## Solutions:

Java:

```java

public class Solution {
    
    public int solve(ArrayList<Integer> A) 
    {
        int root = Integer.MIN_VALUE;
        Stack<Integer> stack = new Stack<>();
        
        for (int num : A)
        {
            // values appear after root has to be greater than root value
            if (num < root)
                return 0;
            
            // update root as last greater value (next root of right subtree)
            while (!stack.isEmpty() && stack.peek() < num)
                root = stack.pop();
            
            stack.push(num);
        }
        
        return 1;
    }
}
```

C++:

```cpp

int Solution::solve(vector<int> &A) 
{
    int root = INT_MIN;
    
    stack<int> stk;
    
    for (auto num : A)
    {
        if (num < root) return 0;
        
        for (;!stk.empty() && stk.top() < num; 
                root = stk.top(), 
                stk.pop());
        
        stk.push(num);
    }
    
    return 1;
}
```
