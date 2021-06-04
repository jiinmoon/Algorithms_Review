# 22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

---

We can use backtracking algorithm to generate all possible combinations. To do
so, at every recursion depth, we keep track of our current open brackets so
that we know to add the matching closing bracket. Base case of our recursion
would be where we have added n pairs.

---

Python:

```python

class Solution22:

    def generateParentheses(self, n):

        def backtrack(open, pair, path):
            # base case: no more pairs to add 
            if open == closed == 0:
                result.append(path)
            else:
                # open bracket needs to be closed
                if open:
                    backtrack(open - 1, pair, path + ")")
                # more pairs to add
                if closed:
                    backtrack(open + 1, pair - 1, path + "(")

        result = []
        backtrack(0, n, "")
        
        return result
```

Java:

```java

class Solution22
{
    public List<String> generateParentheses(int n)
    {
        List<String> result = new ArrayList<>();
        backtrack(0, n, new StringBuilder(), result);
        return result;
    }

    private void backtrack(int open, int pair, StringBuilder path, List<String> result)
    {
        if (open == 0 && pair == 0) {
            result.add(path.toString());
        } else {
            if (open != 0) {
                path.append(")");
                backtrack(open - 1, pair, path, result);
                path.deleteCharAt(path.length()-1);
            }

            if (pair != 0) {
                path.append("(");
                backtrack(open + 1, pair - 1, path, result);
                path.deleteCharAt(path.length()-1);
            }
        }
    }
}

```
