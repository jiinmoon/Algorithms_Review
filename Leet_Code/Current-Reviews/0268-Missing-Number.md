# 268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return
the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space
complexity and O(n) runtime complexity?

---

If there is only a single element missing in this array, then we can find the
element by finding the expected sum of the array - the actual sum of the array.

O(n) in time complxity to iterate twice to find the sums.

--

Python:

```python

class Solution268:

    def missingNumber(self, nums):

        expected = sum(i for i in range(len(nums) + 1))
        actual = sum(num)

        return expected - actual

```
