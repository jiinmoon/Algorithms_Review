# LeetCode Daily Challenge: August Week.1 - Day.5

## Question

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

```
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
```

## Solution

The trick to solve this question without extra space and in linear runtime is
noticing that the elements appear has bound of the length of the array. Thus,
we can use the array index itself as an indicator of whether the element is
present or not as well as detecting duplicates.

Python:

```python
class Solution:
    def findDuplicates(self, nums):
        res = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                res.append(num)
            nums[abs(num)-1] *= -1
        return res
```
