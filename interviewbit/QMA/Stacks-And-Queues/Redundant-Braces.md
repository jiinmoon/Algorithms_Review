# Redundant Braces

Given a string A denoting an expression. It contains the following operators
’+’, ‘-‘, ‘*’, ‘/’.

Chech whether A has redundant braces or not.

Return 1 if A has redundant braces, else return 0.

Note: A will be always a valid expression.

---

Here, we can use stack to keep track of balances of the braces. When closing
brance is encountered, we start to look behind in our stack. We have a case of
valid brace so long as we can find the operators inbetween the braces. Thus,
when we are poping from stack, we check that we have at least a single operator
present. If we do, we can continue. Otherwise, we conclude that we have invalid
expression. O(n) in both time and space complexity.

---

Python:

```python

class Solution:

    def braces(self, A):

        stack = []

        for char in A:

            if char == ')':

                top = stack.pop()
                notValid = True
                
                # redundant if no operator is found in between
                while top != '(':
                    if top in {'+', '-', '*', '/'}:
                        notValid = False
                    top = stack.pop()
                
                if notValid:
                    return 1

            else:
                stack.append(char)

        return 0

```
