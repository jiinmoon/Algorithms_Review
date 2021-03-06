# 301. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input
string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

---

We use backtrack to consider at every position and parenthesis encountered, and
build the path as we remove them as indicated by the counter of invalid
parentheses that we have built in the beginning. To start, we iterate to find
the number of parentheses that are invalid. If the current character is open
parenthesis, we increment counter for left side as matching closing parenthesis
can be found later to update it. If it is closing parenthesis, we check for
whether matching open parenthesis is found - if not, increment the right
counter and update the left.

Now that we have a number of left and right counts of parenthesis to remove, we
use backtrack to build the path. Starting at each index, we recursively
traverse down. If the pointer reaches the end, we check to see our remaining
invalid counts - if both are 0, we can add this path to our result.

Otherwise, we have to remove the parenthesis that are pointed by the current
index. If it is open or closing, decrement the remaining counts and recursively
backtrack to build to next path.

It could be that current character is not parenthesis. In which case, we simply
ignore and move onto the next character. If the current character is
parenthesis, increment the count that we have seen thus far and move on.

Since at each index, we have to consider removal or not, this is a O(2^n) in
time complexity.

---

Java:

```java

class Solution {

    public List<String> removeInvalidParentheses(String s) {
        int invalidOpen = 0;
        int invalidClosed = 0;

        for (char c : s.toCharArray()) {
            if (c == '(')) invalidOpen++;
            else if (c == ')') {
                if (invalidOpen > 0) invalidOpen--;
                else invalidClosed++;
            }
        }

        Set<String> result = new HashSet<>();
        helper(new StringBuilder(), 0, 0, 0, invalidOpen, invalidClosed, s, result);

        return new LinkedList<>(result);
    }

    public void helper(StringBuilder path, int i, int l, int r, int lRem, int rRem, String s, Set<String> result) {
        // base case; index reached end of string
        // should have removed all invalid parentheses
        if (i == s.length()) {
            if (lRem == 0 && rRem == 0)
                result.add(path.toString());
            return;
        }

        // current character is either open or closed paren
        // consider removing them first
        char curr = s.charAt(i);
        
        if (curr == '(' && lRem > 0)
            helper(path, i+1, l, r, lRem-1, rRem, s, result);
        else if (curr == ')' && rRem > 0)
            helper(path, i+1, l, r, lRem, rRem-1, s, result);

        // 3 cases:
        // it is normal character or parentheses we just added to path
        path.append(curr);
        if (curr != '(' && curr != ')')
            helper(path, i+1, l, r, lRem, rRem, s, result);
        else if (curr == '(')
            helper(path, i+1, l+1, r, lRem, rRem, s, result);
        // close only when more open were added previously
        else if (curr == ')' && l > r)
            helper(path, i+1, l, r+1, lRem, rRem, s, result);

        path.deleteCharAt(path.length()-1);
    }
}

```

Python:

```python

class Solution:
    def removeInvalidParentheses(self, s):
        def helper(path, idx, lCount, rCount, lRemain, rRemain):
            # reached the end and all marked parenthesis are removed
            if idx == len(s):
                if not (lRemain or rRemain):
                    result.add("".join(path))
                return

            # first, consider removing currently encountered open/closed
            # parenthesis so long as we can remove them
            if s[idx] == "(" and lRemain:
                helper(path, idx + 1, lCount, rCount lRemain - 1, rRemain)
            elif s[idx] == ")" and rRemain:
                helper(path, idx + 1, lCount, rCount, lRemain, rRemain - 1)
            
            # once removed, we build our path
            path.append(s[idx])

            # backtrack further considering left and right valid counts built thus far
            # if neither parenthesis, simply move on
            if s[idx] != "(" and s[idx] != ")":
                helper(path, idx + 1, lCount, rCount, lRemain, rRemain)
            # if open parenthesis, increment left count and move on
            elif s[idx] == "(":
                helper(path, idx + 1, lCount + 1, rCount, lRemain, rRemain)
            # currently added parenthesis was closing one and we had more
            # open than closing added thus far; move onto by adding right count
            elif s[idx] == ")" and lCount > rCount:
                helper(path, idx + 1, lCount, rCount + 1, lRemain, rRemain)

            # current path is finished; prepare for next
            path.pop()
        
        # iterate to find the number of invalid parentheses to remove from left and right
        l, r = 0, 0
        for char in s:
            if char == "(":
                l += 1
            elif char == ")":
                # if no matching opening parenthesis, mark right for removal
                # if matching opening parenthesis, remove left as it is valid
                if l: l -= 1
                else: r += 1
        
        result = set()
        helper([], 0, 0, 0, l, r)
        return result
```
