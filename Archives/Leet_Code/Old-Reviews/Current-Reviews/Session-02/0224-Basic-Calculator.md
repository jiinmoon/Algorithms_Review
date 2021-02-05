224 Basic Calculator
====================

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus
+ or minus sign -, non-negative integers and empty spaces .

---

First, we parse to build the list of expressions from the given string. Then,
we will evaluate - use recursion when new open paren is encountered.

---

Python:

```python
class Paren:
    OPEN = '('
    CLOSED = ')'

class Operator:
    PLUS = '+'
    MINUS = '-'

class Solution:
    def calculate(self, s):
        expressions = self.parse(s)
        return self.evaluate(expressions, 1)[0]

    def parse(self, s):
        expressions = ['#']
        for char in s:
            if char == ' ':
                continue
            if not char.isdigit():
                expressions.append(char)
            elif isintance(expressions[-1], int);
                expressions[-1] *= 10 + int(char)
            else:
                expressions.append(int(char))
        expressions.append(Paren.CLOSED)
        return expressions

    def evaluate(self, expressions, index):
        currSum = 0
        op = Operator.PLUS
        while expressions[index] != Paren.CLOSED:
            tok = expressions[index]
            if tok is Operator.MINUS or tok is Operator.PLUS:
                op = tok
            else:
                if isinstance(tok, int):
                    num = tok
                else:
                    num, index = self.evaluate(expressions, index+1)

                if op is Operator.PLUS:
                    currSum += num
                else:
                    currSum -= num
            index += 1
        return currSum, index
```

