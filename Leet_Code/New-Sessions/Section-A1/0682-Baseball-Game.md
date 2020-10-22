# 682 Baseball Game

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

We can use stack to maintain our scores which will be summed up in the end
- this should be O(n) in both time and space complexity.

Note that integers are between 0 - 9 and _it can be negative_. 

---

Python:

```python

class Solution:
    def calPoints(self, ops):
        stk = []
        for char in ops:
            # integer can be negative
            if char.lstrip("-").isdigit():
                stk.append(int(char))
            elif char == "+":
                x, y = stk.pop(), stk.pop()
                stk += [y, x, x + y]
            elif char == "D":
                stk.append(stk[-1] * 2)
            elif char == "C":
                stk.pop()

        return sum(stk)
```
