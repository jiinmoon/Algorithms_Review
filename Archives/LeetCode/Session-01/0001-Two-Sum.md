# 1. Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

---

First naive approach to this problem would be to brute force comparison of an
element against every other element to see whether two chosen elements would
add upto the sum. This would be O(n^2) in time complexity due to nested loop
involved; however, would require no additional space complexity.

Slight improvement can be made by first sorting the given array of integers. By
doing so, we can use two pointer approach - have two pointers at either end,
and move inwards depending on our current sum. Sorting would take O(n * log(n))
time complexity and two pointer scan would be O(n) in time complexity - hence,
overall would be O(n * log(n)) in time complexity. The space complexity depends
upon the sorting algorithm used but can be constant.

To achieve best time complexity, we need to trade up space - in particular, we
use hashmap to store the previously seen elements and access them in O(1) time
complexity. This would be O(n) in time complxity, but also O(n) in space
complexity as well.

---

Python: Hashmap approach.

```python

class Solution1:

    def findTwoSum(self, nums, target):

        m = {}

        for i, num in enumerate(nums):
            if num in m:
                return [m[num], i]
            else:
                m[target - num] = i
        
        return []
```

Java: Hashmap approach.

```java

class Solution1
{
    public int[] findTwoSum(int[] nums, int target)
    {
        HashMap<Integer, Integer> m = new HashMap<>();

        for (int i = 0; i < nums.length; i++)
        {
            if (m.containsKey(nums[i]))
                return new int[] {m.get(nums[i]), i};

            m.put(target - nums[i], i);
        }

        return new int[] {};
    }
}
```
