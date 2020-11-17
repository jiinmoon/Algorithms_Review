# 31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest
possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

---

Naive approach would be to generate all permutations in order until we have
seen the given permutation - then generate one step further. As there are n!
permutations possible, the time complexity would be proportionally great.

Another approach requires a trick to reailize that next permutation depends
upon the state of current permutation. If the given permutation is in order,
then next state is the reverse of the current. Otherwise, we can find the first
element that is out of order from the end, then swap it with the next greater
value in that subarray where the first out of order value was found. Then, this
subarray is reversed to produce the next permutation. This will be O(n) in time
complexity due to reverse process and constant as this can take place in order.

---

Python:

```python

class Solution:
    def nextPermutation(self, nums):
        m = len(nums)
        i = m - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = m - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        self.reverse(nums, i + 1)

    def reverse(self, nums, start):
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
```
