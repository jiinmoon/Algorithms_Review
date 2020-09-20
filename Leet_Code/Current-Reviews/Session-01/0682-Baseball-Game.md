682 BaseBall Game
=================

Given a list of strings, they represents following:

1. Integer: represents a score for this round.

2. "+": represents score for this round is sum of previous two rounds.

3. "D": represents score that is double of previous round.

4. "C": represents a cancel; removes previous round's score.

Return sum of all rounds scores.

---

We may use a simple stack to keep track of the scores. Pay particular
attention to handling negative integers, and how we pop the elements.

---

Python:

```python

class Solution:
    def calPoints(self, ops):
        stk = list()
        for tok in ops:
            # handle negative integers as well
            # isdigit cannot detect -int
            if tok.lstrip('-').isdigit():
                stk.append(int(tok))
            elif tok == '+':
                a, b = stk.pop(), stk.pop()
                stk += [b, a, a + b]
            elif tok == 'D':
                stk.append(stk[-1] * 2)
            elif tok == 'C':
                stk.pop()

        return sum(stk)
```
