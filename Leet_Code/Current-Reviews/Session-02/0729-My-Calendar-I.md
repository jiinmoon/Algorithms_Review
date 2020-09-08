729 My Calendar I
=================

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

Simply, we maintain a list of intervals where we have booked using a tuple of
(startTime, endTime).

Then, whenever `book(start, end)` is called, we can perform binary search to
find the insert position for the current (start, end).

Either there is no overlapp between the intervals found at i-1 and i or it is
already booked and cannot be inserted without modifying the intervals
(merging). Hence, we return False in such case.

Otherwise, we insert the new interval at its rightful place.

---

Python:

```python
class Solution:
    def __init__(self):
        # initial intervals as guards (prevent idx out of bounds)
        self.intervals = [
            (float('-inf'), float('-inf)),
            (float('inf'), float('inf))
        ]

    def book(self, start, end):
        i = bisect.bisect_left(self,intervals, (start, end))
        if start < self.intervals[i-1][1] or self.intervals[i][0] < end:
            return False
        self.intervals.insert(i, (start, end))
        return True
```
