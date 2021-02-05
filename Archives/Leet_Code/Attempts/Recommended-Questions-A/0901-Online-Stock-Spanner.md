# 901. Online Stock Spanner

Write a class StockSpanner which collects daily price quotes for some stock,
and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of
consecutive days (starting from today and going backwards) for which the price
of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60,
70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

---

We maintain the stock and its span in a stack. By doing so, we can update the
previous span counts by popping from the stack while its price is less than the
current price introduced.

---

Java:

```java

import java.util.LinkedList;

class StockSpanner {
    
    static class Pair {
        private int price, span;

        public Pair(int price, int span) {
            this.price = price;
            this.span = span;
        }
    }

    private Deque<Pair> stk;

    public StockSpanner() { this.stk = new LinkedList<>(); }

    public int next(int price) {
        int span = 1;

        while (!this.stk.isEmpty() && this.stk.peekLast().price <= price) {
            Pair prev = this.stk.removeLast();
            span += prev.span;
        }

        this.stk.addLast(new Pair(price, span));
        return span;
    }
}


```


Python:

```python

class StockSpanner:
    def __init__(self):
        self.stk = list()

    def next(self, price):
        span = 1
        while self.stk and self.stk[-1][1] <= price:
            prevSpan, _ = self.stk.pop()
            span += prevSpan
        self.stk.append((span, price))
        return span
```
