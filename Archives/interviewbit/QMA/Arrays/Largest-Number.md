# Largest Number

Given a list of non negative integers, arrange them such that they form the
largest number.

---

Use a custom comparator where we can sort the given elements by comparing two
cases: given A and B, compare which generates greater value, A + B or B + A.

O(n * log(n)) time complexity due to sorting involved.

---

Python:

```python

from functools import cmp_to_key

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        
        def larger(x, y):
            if x + y > y + x:
                return -1
            return 1
            
        nums = list(map(str, A))
        nums.sort(key=cmp_to_key(larger))

        while len(nums) > 1 and nums[0] == '0':
            nums = nums[1:]

        return "".join(nums)
```
