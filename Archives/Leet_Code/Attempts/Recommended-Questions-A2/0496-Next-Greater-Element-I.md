# 496. Next Greater Element I

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
elements are subset of nums2. Find all the next greater numbers for nums1's
elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to
its right in nums2. If it does not exist, output -1 for this number.

---

Naive approach would be to for each element in nums1, we scan the nums2 for
next greater element. Time complexity would be nested, hence O(n * m).

We can reduce the complexity by using extra structure; here, we use stack to
only keep track of the maximum values that we have seen thus far. For every num
in nums2, we check against the stack to see whether it is a current maximum.
Then, previous smaller number should be on top of the stack, in which case, we
check against the nums1 to see whether the smaller number exist.

Time complexity would be linear O(len(nums2)) and it takes as much space as the
length of nums1.

---

Python:

```python

class Solution496:

    def nextGreater(self, nums1, nums2):

        m = {num:i for i, num in enumerate(nums1)}

        result = [-1 for _ in range(len(nums1))]
        stk = list()

        for num in nums:
            while stk and stk[-1] < num:
                temp = stk.pop()
                if temp in m:
                    result[m[temp]] = num
            stk.append(num)

        return result
```
