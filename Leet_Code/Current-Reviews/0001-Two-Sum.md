# 1. Two Sum

Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

---

(1) Brute Force.

Use nested loops to compare each element against others to check whether two
elements sum upto the target value. This would be O(n^2) in time complexity and
O(1) in sapce complexity.

(2) Sort + Two Pointers.

By sorting the array, we can use two pointers placed at left and right to check
for their sum. Sorting takes O(n * log(n)) in time complexity even though two
pointers will take O(n). Space complexity would depend upon sorting algorithm
used but if in-place sorting is used, O(1).

(3) Hashmap.

By recording the previous values in the hashmap, we can check for membership of
the element in O(1) time. Thus, this will reduce the time complexity to O(n)
but space will also take O(n).

---

Python:

```python

class Solution1:

    def twoSum(self, nums, target):
        
        d = dict()

        for i, num in enumerate(nums):

            if num in d:
                return [d[num], i]
            d[target - num] = i

        return []
```

Java:

```

class Solution1 {

    public int[] twoSum(int[] nums, int target)
    {
        Map<Integer, Intger> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++)
        {
            if (map.containsKey(nums[i]))
                return new int[] { map.get(nums[i]), i };
            map.put(target - nums[i], i);
        }

        return new int[] {};
    }
}

```
