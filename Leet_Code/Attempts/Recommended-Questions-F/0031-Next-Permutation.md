# 31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest
possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

---

Naive approach would be to actually permutate the given list of numbers to find
the next permutation.

But here, we have a pattern that we can utilize to find the next permutation in
O(n) time complexity. First, we start from the end of the given list to find
the first value that is not in order (marks the first element to be incremented
for next permutation).

Two possible cases present, we either find this value which indicates that the
permutation lies within the given number - in which case, we swap the found
value with the next greater value starting from the index of the found value;
or, entire list is in correct order - which means that the next permutation is
the reverse order.

---

Python:

```python

class Solution:
    def nextPermutation(self, nums):
        m = len(nums)
        i = m - 2
        # find first out-of-place element from behind
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        
        # two cases: 
        # 1. element is found - list is unordered
        # 2. element is not found - list is ordered
        if i >= 0:
            # find next greater element starting from i to swap
            j = m - 1
            while j > 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # either case, reverse entire list for next permutation start from i
        self.reverseArr(nums, i + 1)

    def reverseArr(self, nums, start):
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
```
