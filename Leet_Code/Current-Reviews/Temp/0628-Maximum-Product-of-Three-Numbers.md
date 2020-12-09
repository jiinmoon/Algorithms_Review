# 628. Maximum Product of Three Numbers

Given an integer array nums, find three numbers whose product is maximum and
return the maximum product.

---

#### (1) Sort first.

Maximum product of three numbers are either product of three largest numbers or
one largest number with two smallest numbers within the array. As we want to
identify 5 elements, we can do this via sorting the array first. This would be
O(n * log(n)) in time complexity and O(1) if in-place sorting is used.

#### (2) Iterate to identify 5 elements.

Since we only want 5 elements, we can search them in linear fashion in a single
iteration on the array. O(n) in time complexity.

---

Python: Iterate.

```python

class Solution628:
    
    def maxProduct(self, nums):

        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:
            
            # find max1, max2 and max3
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            # find min1 and min2
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, max1 * min1 * min2)

```

Python: Sort.

```python

class Solution628:

    def maxProduct(self, nums):

        nums.sort()

        return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[0] * nums[1])

```
