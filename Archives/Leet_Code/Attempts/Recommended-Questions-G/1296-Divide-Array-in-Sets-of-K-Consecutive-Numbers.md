# 1296. Divide Array in Sets of K Consecutive Numbers

Given an array of integers nums and a positive integer k, find whether it's
possible to divide this array into sets of k consecutive numbers.

Return True if its possible otherwise return False.

---

The efficient approach would be to try to group the numbers in consecutive
fashion. Once each window has reached their length, we remove it from our
group. If the total group is empty at the end, we can indeed form into
individual sets of k consecutive numbers.

To do so, we use heap and sorting strategy. By sorting the array first, we can
build our consecutive windows easily by iterating from left to right without
having to check for their counts or membership. Here, we do not have to
maintain entire window at all - all we require to maintain is the last value of
the window and its current window length to see whether it has reached k or
not. By using minheap, we are guranteed to build our windows from smallest.

Sort the array and examine each of the numbers. If there are no windows present
or it is a duplicate value on top of our heap, then this form a start of new
window.

Then, we can check to see whether current number can be extended on our current
window (is last value from current window 1 smaller than current number to
add?). If it cannot, we early exit and decide entire operation is impossible.

Otherwise, we can update our min heap - if it has reached its size k, we remove
from our windows, otherwise, push back in the heap with updated last value
(current number) and length + 1.

Due to sorting involved, time complexity would be O(n * log(n)), and space
complexity would be O(n).

Another method that is similar in approach that does not involve heap is simply
use hashmap to record count of each elements first. From sorted array, consider
each num as a starting position. Then, there should be enough counts for
element ranging from current number to current number + k.

---

Python: hashmap approach.

```python

class Solution:
    def isPossibleDivide(self, hand, W):
        if not hand or not W or len(hand) % W:
            return False

        counter = collections.Counter(hand)
        
        # consider each num as starting position
        for srt in sorted(counter.keys()):
            count = counter[srt]
            # current number has been used up previously
            if not counter[srt]:
                continue
            # all elements from srt to srt + W must be present in counter
            for i in range(srt, srt + W):
                if i not in counter or counter[i] < count:
                    return False
                counter[i] -= count

        return True
```

Python: heap approach.

```python

import heapq

class Solution:
    def isPossibleDivide(self, hand, W):
        if not hand or not W or len(hand) % W:
            return False
        
        # each window records (lastVal, length)
        windows = list()

        for num in sorted(hand):
            # new sequence starting from num found
            if not windows or windows[0][0] == num:
                heappush(windows, (num, 1))
                continue
            # current num cannot extend current window
            if num - 1 != windows[0][0]:
                return False
            # update windows
            _, length = heappop(windows)
            # if adding current will reach size, remove else add
            if length != W - 1:
                heappush(windows, (num, length+1))

        return not windows
```

