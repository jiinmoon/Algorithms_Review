# 1. Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

---

Finding the two elements in the array that sums to target value can be
approached with a hashmap structure where we will record the previously
encountered elements. This algorithm will be O(n) in both time and space
complexity.

---

Java:

```java

import java.util.HashMap;

class Solution {
    public int[] findTwoSum(int[] nums, int target) {
        HashMap<Integer, Integer> m = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (m.containsKey(nums[i])) {
                return new int[] { m.get(nums[i]), i };
            };
            m.put(target - nums[i], i);
        };
        return new int[] {};
    }
}
```

Python:

```python

class Solution:
    def findTwoSum(self, nums, target):
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            d[target - num] = i
        return []
```
