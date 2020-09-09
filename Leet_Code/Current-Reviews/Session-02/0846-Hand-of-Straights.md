846 Hand of Straights
=====================

Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W,
and consists of W consecutive cards.

Return true if and only if she can.

---

We will try to build up the straights from the given array of integers.

First, we will sort the array such that we can build in consecutive order - and
it allows us to detect whether the number is broken.

We will maintain a heap of tuple, (lastNum, straightLength). So as we examine
the value in the order, we can first check whether current value is either
first subsequence to build or equal to the first value in our heap. If it is
equal, it indicates a case where we have multiple of same values which should
belong to a separte group. In these cases, we can create a new tuple with
current num - indicating new straights to build.

But suppose that current value is greater than first value in the heap by more
than 1, then this breaks the consecutive sequence and straight is broken. We
cannot complete the task.

Otherwise, we take the minimum (lastNum, straightLength) from the heap. Then,
we check whether adding current num to this straight completes this straight
with length W. If not, we update the lastNum and increase the length and push
back into the heap.

In the end, the heap should have no partially completed straights leftover.

The time complexity of this algorithm is O(n * log(n)) where for each element,
we may have to perform heappop and heappush.

---

Python:

```python
import heapq

class Solution:
    def isNStriaghtHand(self, hand, N):
        if not hand or not N or len(hand) % N:
            return False
        if N == 1:
            return True

        hand.sort()
        pq = list()

        for num in nums:
            # duplicate value or new straight to build
            if not pq or pq[0][0] == num:
                heappush(pq, (num, 1))
                continue
            
            # breaks the current straight
            if num > pq[0][0] + 1:
                return False

            _, handLength = heappop(pq)
            if handLength < W - 1:
                heappush(pq, (num, handLength+1))

        return not pq
```
