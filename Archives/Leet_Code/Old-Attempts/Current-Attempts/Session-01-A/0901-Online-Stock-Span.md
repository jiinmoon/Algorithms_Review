# 901 Online Stock Span

Use stack to maintain the cumulative span for the price.

---

Python:

```python

class StockSpanner:
    def __init__(self):
        self.stk = list()

    def next(self, price):
        span = 1
        while self.stk and self.stk[-1][0] <= price:
            _, prevSpan = self.stk.pop()
            span += prevSpan
        self.stk.append((price, span))
        return span
```
