# 202. Happy Number

Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

---

#### 1. Using Set.

By using set, we can try to iterate the problem until we have seen the
duplicate element (cycle) or reached 1. O(log(n)) in time complexity as the
number of digits to process at each step reduces logrithmically. Space
complexity is identical to store all the previous results.

#### 2. Using Cycle Detection algorithm.

By using Floyd-Warshall, we can find whether there exist a cycle - which slow
and fast converges on the same point or number can reduce to 1 in which case
fast escapes the loop by reaching the end or 1.

O(log(n)) in time complexity since it borrows the same idea as above but O(1)
in space.

---

Python: Floyd-Warshall.

```python

class Solution202:

    def isHappy(self, num):

        def next(num):
            result = 0
            while num:
                num, d = divmod(num, 10)
                result += d ** 2
            return result

        slow, fast = num, next(num)
        
        # either fast can escape the loop or
        # cycle is detected (slow == fast)
        while fast != 1 or slow == fast:
            slow = next(slow)
            fast = next(next(fast))

        return fast == 1
```
