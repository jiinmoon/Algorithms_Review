# 3 Sum

Given an array S of n integers, find three integers in S such that the sum is
closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

---

To find the closest three candidates, we first sort the array, then use the two
pointers. As we have to find two candidates for one element chosen in outer
loop, time complexity is O(n^2).

---

Python:

```python

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, nums, target):
        if not nums or len(nums) < 3:
            return []
        if len(nums) == 3:
            return sum(nums)
        
        nums.sort()
        
        closestDiff = float('inf')
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1
            while j < k:
                currSum = nums[i] + nums[j] + nums[k]
                if abs(target - currSum) < abs(closestDiff):
                    closestDiff = target - currSum
                if currSum < target:
                    j += 1
                else:
                    k -= 1
            if closestDiff == 0:
                break
        return target - closestDiff
```
