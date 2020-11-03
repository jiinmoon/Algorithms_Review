# 682. Baseball Game

You are keeping score for a baseball game with strange rules. The game consists
of several rounds, where the scores of past rounds may affect future rounds'
scores.

At the beginning of the game, you start with an empty record. You are given
a list of strings ops, where ops[i] is the ith operation you must apply to the
record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is
guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed
there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is
guaranteed there will always be a previous score.

Return the sum of all the scores on the record.

---

Since the scores that we wish to track depends upon previous values, we can use
stack and its LIFO nature to easily manipulate the scores. The time complexity
should be O(n).

---

Python:

```python

class Solution:
    def calPoints(self, ops):
        stk = list()
        for op in ops:
            if op.lstrip('-').isdigit():
                stk.append(int(op))
            elif op == "+":
                a, b = stk.pop(), stk.pop()
                stk += [b, a, a + b]
            elif op == "D":
                stk.append(stk[-1] * 2)
            elif op == "C":
                stk.pop()
        
        retrun sum(stk)
```
