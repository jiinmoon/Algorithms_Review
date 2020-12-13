# Sliding Window Maximum

Given an array of integers A. There is a sliding window of size B which
is moving from the very left of the array to the very right.
You can only see the w numbers in the window. Each time the sliding window
moves rightwards by one position. You have to find the maximum for each window.

---

We can use a deque or linked list with access to head and tail to maintain our
window. Iterating forward, we check our last value of the window against
current value. Since we only wish to maintain maximum values, we pop from our
window all the values less than current. Then we add the current to extend our
window and check to see that it has the correct size. Otherwise, we remove the
first value. So long as size requirement is met, we can add our current maximum
of the sliding window which is the first element to our result list. O(n) in
both time and space complexity.

---

Python:

```python

from collections import deque

class Solution:

    def slidingMaximum(self, A, B):

        queue = deque()
        result = list()

        for i, num in enumerate(A):

            while queue and A[queue[-1]] < num:
                queue.pop()

            queue.append(i)

            if q[0] <= i - B:
                queue.popleft()

            if i >= B - 1:
                result.append(A[queue[0]])

        return result
```
