# 224 Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus
+ or minus sign -, non-negative integers and empty spaces .

---

The main difficulty with the problem is dealing with the recursive algorithm of
handling the open and closing parentheses.

But first, we should parse the given expression into tokens based on the cases
- for each character in the string, the character can either be

1. Space; in which case, we skip the character.

2. If it is not a digit, we can conclude it is either parentheses or operator;
   which is safe to add to our list of tokens.

3. If it is a digit, we need to expand as far out as possible since the number
   can be multidigit. And add onto the list.

When we have a list of tokens, we compute the tokens via recursive calls as we
iterate on the list. This will involve maintain the current index of the tokens
as well as current sum of the computed values so far.

So long as the encountered token is not the closed parentheses which signals
the end of the computation (given list of tokens will itself be surrounded by
the open and closed parentheses by the parser to act as a guard), we can
evaluate the token based on following cases:

1. Token is an operator, which is either plus or minus. In this case, we update
   our operator value to token.

2. If it is not plus or minus, then we can conclude it is either bracket or
   number. So, if is is number, then record the number. If not, it is opening
   bracket to signal the recursive call to itself to update both the number and
   the index. Once the number is obtained, we can perform the operation based
   on the operator.

---

Python:

```python

class Solution:
    def calculate(self, s):
        tokens = self.parse(s)
        return self.compute(tokens, 1)[0]

    def parse(self, s):
        # surround given expression with ( ... ) to act as a guard during
        # computation phase
        for tok in s:
            if tok == " ":
                continue
            elif not tok.isdigit():
                tokens.append(tok)
            # extend from previous number
            elif tok and isinstance(tok[-1], int):
                tokens[-1] *= 10 + int(tok)
            else:
                tokens.append(int(tok))

        return "(" + tokens + ")"

    def evaluate(self, tokens, idx):
        currSum = 0
        op = "+"
        while tokens[idx] != ")":
            tok = tokens[idx]

            if tok == "+" or tok == "-":
                op = tok
            else:
                if isinstance(tok, int):
                    num = tok
                else:
                    num, idx = self.evaluate(tokens, idx + 1)

                if op == "+":
                    currSum += num
                else:
                    currSum -= num

            idx += 1

        return currSum, idx
```
