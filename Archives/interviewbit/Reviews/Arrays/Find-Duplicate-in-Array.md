# Find Duplicate in Array

Given a read only array of n + 1 integers between 1 and n, find one number that
repeats in linear time using less than O(n) space and traversing the stream
sequentially O(1) times.

---

The particular quality about the elements present within the array that the
elements are bounded by the length of the array allows us to use cycle
detection algorithm. Since there are duplicated element, it will continue to
loop and revisit the same index over and over as we traverse through the array
and by its index denoted by the elements.

We first use Floyd's Cycle Detection algorithm by setting up slow and fast
runners. Both will runner forward until cycle has been found. Then, to find
where the cycle begins which is the one number that repeat, start searching
again from the beginning and iterate forward until both pointers meet.

O(n + k) in time complexity where k is the length of the cycle.

---

Python:

```python

class Solution:

    def findDuplciates(self, arr):

        slow, fast = arr[0], arr[arr[0]]

        while True:

            slow = arr[slow]
            fast = arr[arr[fast]]
            
            # cycle has been found
            if slow == fast:

                # iterate from beginning to find the start of cycle
                fast = 0
                while slow != fast:
                    slow = arr[slow]
                    fast = arr[fast]

                return fast
```
