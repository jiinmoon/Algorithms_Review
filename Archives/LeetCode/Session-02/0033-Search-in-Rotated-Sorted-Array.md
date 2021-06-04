# 33. Search in Rotated Sorted Array

Given the array nums after the rotation and an integer target, return the index
of target if it is in nums, or -1 if it is not in nums.

---

Even though the array is rotated about some unknown pivot, the array itself is
still in order. This implies that we may still use the principle of binary
search as we can first divide the array into halfs, and check whether lower or
upper half of the array is in sorted order. Then, we can check whether target
value lies in the sorted half's boundary. This can achieve O(n * log(n)) in
time complexity.

---

Python:

```python

class Solution33:
    
    def searchRotated(self, nums, target):

        l, r = 0, len(nums) - 1

        while l <= r:
            
            mid = l + (r - l) * 0.5

            if nums[mid] == target:
                return mid

            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
```

