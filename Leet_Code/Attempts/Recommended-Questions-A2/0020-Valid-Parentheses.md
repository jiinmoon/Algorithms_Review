# 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

---

We use stack to look behind our order of pushed in opening brackets - if
current character is closing, then top of our stack must match the opening
brackets. In the end, the stack has to be empty.

---

Java:

```java

class Solution20 {
    
    private Map<Character, Character> map;
    
    public boolean isValid(String s) {
        
        this.map = new HashMap<>();
        this.map.put(')', '(');
        this.map.put(']', '[');
        this.map.put('}', '{');
        
        char[] chars = s.toCharArray();
        Stack<Character> stack = new Stack<>();
        
        for (char c : chars)
        {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty() || stack.peek() != this.map.get(c))
                    return false;
                stack.pop();
            }
        }
        
        return stack.isEmpty();
    }
}

```

Python:

```python

class Solution20:
    
    def __init__(self):
        self.m = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
    def isValid(self, s: str) -> bool:
    
        stack = list()
        
        for char in s:
            if char in {"{", "[", "("}:
                stack.append(char)
            else:
                if not stack or stack[-1] != self.m[char]:
                    return False
                stack.pop()
        
        return not stack
```
