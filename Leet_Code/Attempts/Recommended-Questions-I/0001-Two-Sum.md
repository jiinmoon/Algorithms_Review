# 1. Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

---

Naive approach involves nested loop comparing each element against one another
in O(n^2) time complexity. Another method would be to sort the array of
integers and use two pointers method, which is O(n * log(n)) in time
complexity. One solution that can achieve best time complexity of O(n) would be
to trade space for time - that is use hashmap to store the previously exaimned
values.

---

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

C++:

```cpp

class Solution {
    public:
        
        vector<int> findTowSum(vector<int>& nums, int target)
        {
            unordered_map<int, int> m;
            for (int i = 0; i < nums.size(); i++)
            {
                if (m.find(nums[i]) != m.end())
                    return { m.find(nums[i])->second, i };
                m.emplace(target - nums[i], i)
            }
            return {};
        }
}
```
