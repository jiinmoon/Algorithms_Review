# 682 Baseball Game

You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get
in this round.
"+" (one round's score): Represents that the points you get in this round are
the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are
the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid
round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round
before and the round after.

You need to return the sum of the points you could get in all the rounds.

---

We use stack to maintain the each round's point depending on the char
encountered as we iterate on the given list of strings. If it is an integer, we
simply push onto stack. If it is "+", then we pop two values from stack, add
them, and push them all back in order. If it is "D", then double the previous
round's score. If it is "C", then pop from the stack.

---

Python:

```python

class Solution:
    def baseballGame(self, ops):
        stack = list()

        for op in ops:
            if op.lstrip('-').isdigit():
                stack.append(int(op))
            elif op == "+":
                a, b = stack.pop(), stack.pop()
                stack += [b, a, a + b]
            elif op == "D" and stack:
                stack.append(stack[-1] * 2)
            elif op == "C" and stack:
                stack.pop()

        return sum(stack)
```
