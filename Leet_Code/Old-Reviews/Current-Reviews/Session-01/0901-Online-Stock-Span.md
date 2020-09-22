901 Online Stock Span
=====================

Write a class StockSpanner which collects daily price quotes for some stock,
and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of
consecutive days (starting from today and going backwards) for which the price
of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60,
70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

---

We can use a stack to maintain the (price, spanThusFar) for each of the price
that were pushed with `next()`. So, when next() is called, we can repeatedly
pop from the stack until the top of the stack price is less than the itself
- and the span of this price would be the sum of all the spans that that we had
  to pop from the stack to maintain "consecutive span". And when we found it,
  we can push in this price with the updated spance into the stack and return
  result.

---

```python
class StockSpanner:
    def __init__(self):
        self.stk = list()

    def next(self, price):
        spanThusFar = 1
        while self.stk and self.stk[-1][0] <= price:
            (_, prevSpan) = self.stk.pop()
            spanThusFar += prevSpan
        self.stk.append( (price, spanThusFar) )
        return spanThusFar
```
