32 Longest Valid Parentheses
============================

Question:
---------

Given a string containing just the characters from '()', find the longest
substring that consists of well-formed parentheses.

Solutions:
----------

Similar to how we utilized a stack to keep track of well-formed parentheses, we
will again use to determine the length by storing the indicies of the
characters instead. As we iterate on the string, we will push in the indicies
of the open parenthese; and if matching one is found, we pop. This will leave
behind the indicies where it "breaks" the string into segments of well-formed
substrings.

Codes:
------

Python:

```python
class Solution:
    def longestValidParentheses(self, s):
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        longest = 0
        if stack:
            i = len(s)
            while stack:
                j = stack.pop()
                longeset = max(longest, i - j - 1)
                i = j
            longest = max(longest, i)
        else:
            # entire string is valid
            longest = len(s)
        return longest
```

Go:

```go
type idxStack struct {
    indicies []int
}

func (s *idxStack) Push(i int) {
    s.indicies = append(s.indicies, i)
}

func (s *idxStack) Pop() {
    if len(s.indicies) == 0 {
        return
    }
    s.indicies = s.indicies[:len(s.indicies)-1]
}

func (s *idxStack) Top() int {
    return s.indicies[len(s.indicies)-1]
}

func (s *idxStack) IsEmpty() int {
    return len(s.indicies) == 0
}

func max(x, y int) int {
    if x >= y {
        return x
    } else {
        return y
    }
}

func longestValidParenthese(s string) int {
    stack := &idxStack{ indicies : []int{-1} }
    longest := 0

    for i, char := range s {
        if char == "(" {
            stack.Push(i)
            continue
        }
        stack.Pop()
        if stack.IsEmpty() {
            stack.Push(i)
            continue
        }
        longest = max(longest, i - stack.Top())
    }
    return longest
}
``` 

---

**Source:**

LeetCode: [Longest-Valid-Parentheses](https://leetcode.com/problems/longest-valid-parentheses)
