# 729 My Calendar I

Implement a MyCalendar class to store your events. A new event can be added if
adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this
represents a booking on the half open interval [start, end), the range of real
numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie.,
there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be
added to the calendar successfully without causing a double booking. Otherwise,
return false and do not add the event to the calendar.

---

The main problem is identifying whether there is an overlap for the given
interval - and to check it naively, would involve iterating over all the
intervals recorded. To improve upon this, we can use binary search method so
long as we can maintain a list of "valid" intervals sorted. This will
effectively reduce the booking operation down to O(log(n)).

---

Python:

```python

class MyCalendar:
    def __init__(self):
        self.q = [
            (float('-inf'), float('-inf')),
            (float('inf'), float('inf'))
        ]

    def book(self, start, end):
        i = bisect.bisect_left(self.q, (start, end))
        if start < self.q[i-1][1] or self.q[i][0] < end:
            return False
        self.q.insert(i, (start, end))
        return True
```
