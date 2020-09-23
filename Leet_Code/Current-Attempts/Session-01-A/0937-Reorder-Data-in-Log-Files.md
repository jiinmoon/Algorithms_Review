# 937 Reorder Data in Log Files

We create a custom comparator function where we would first sort by the second
log body - is it alpha? Then, we prioritize such logs over the others.

---

Python:

```python

class Solution:
    def reorder(self, logs):
        def logOrder(logs):
            head, body = logs.split(" ", 1)
            if body[0].isalpha():
                return (0, body, head)
            return (1,)
        return sorted(logs, key=logOrder)
```
