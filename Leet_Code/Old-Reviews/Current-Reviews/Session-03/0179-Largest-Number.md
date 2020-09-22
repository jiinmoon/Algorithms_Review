179 Largest Number
==================

Given a list of non-negative integers, arrange them such that they form the
largest number.

---

For example, given "2" and "10", the largest number that we can form would be
"210".

While we could work with the integer form to determine the largest number, the
simplest method would be to actually work with their string format.

By working as string type, we can perform a simple concatenation and easily
perform lexicographical (and numerical) comparison. For example, we can tell
that given "2" and "10", by concatenating two like "210" and "102", we know
which string should take a higher precedence.

Hence, we create a custom comparator and sort the given integer array. Then,
concatenate all the integers.

The exceptional case lies in the fact that there maybe leading zeros.

Time complexity should be time that takes to complete the sort, O(n * log (n)).

---

Python:

```python
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        def largerNumberComparator(a, b):
            return -1 if a + b > b + a else 1

        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(largerNumberComparator))
        while len(nums) > 1 and nums[0] == '0':
            nums = nums[1:]

        return "".join(nums)
```
