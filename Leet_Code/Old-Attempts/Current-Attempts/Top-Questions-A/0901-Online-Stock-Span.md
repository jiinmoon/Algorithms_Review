# 901 Online Stock Span

Write a class StockSpanner which collects daily price quotes for some stock,
and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of
consecutive days (starting from today and going backwards) for which the price
of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60,
70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

---

We can use stack to maintain the previous stock's price and the count of the
cumulative prices. So, when next is called to include a new price, we pop from
the stack so long as top of stack is less than or equal to the price given.
While doing so, we also count the number of counts.

---

Python:

```python

class StockSpanner:
    def __init__(self):
        self.stack = list()

    def next(self, price):
        count = 1
        while stack and stack[-1][0] <= price:
            _, prevCount = stack.pop()
            count += prevCount

        stack.append( (price,count) )
        
        return count
```
