# 1. Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

---

First naive solution to the problem would be to use brute force comparison of
every element against each other. This will involve a nested loop that would
cost O(n^2) in time complexity but no additional space.

Slight improvement can be made by first sorting the given array of integers so
that we can use the two pointer method to find the two elements in linear time.
But due to initial sorting, the time complexity would be bounded by O(n * log(n)).

We can use O(n) space complexity to record each elements that we have seen thus
far - then, we can look up in our record whether for current element, there
exist other element that would add up to the target. For this, hashmap would be
ideal for its O(1) look-up time. Overall, this would be O(n) in both time and
space complexity.

---

Python:

```python

class Solution1:

    def findTwoSum(self, nums, target):

        d = dict()

        for i, num in enumerate(nums):
            if num in d:
                return [ d[num], i ]
            else:
                d[target - num] = i

        return []
```

Java:

```java

class Solution1 {

    public int[] twoSum(int[] nums, int target)
    {
        HashMap<Integer, Integer> m = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++)
        {
            if (m.containsKey(nums[i])
                return new int[] { m.get(nums[i]), i };
            else
                m.put(target - nums[i], i);
        }

        return new int[] {};
    }
}
