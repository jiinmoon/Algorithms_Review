# 1 Two Sum

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

---

Naive solution involves a comparison of choosing every element for every
element. This nested loop approach will take O(n^2) time complexity.

Another approach would be sort the given array of integers, and use two
pointers that start from the either end of the arrays. This gives
a directionality as to whether we are getting closer to the target by moving
one pointer at a time. Due to sorting involved, time complexity is bounded by
O(n * log(n)).

We can achieve O(n) in both time and space complexity via using a hashmap
structue. We use this to record our previous elements.

---

C++:

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i) {
            if (m.find(nums[i]) != m.end()) {
                return { m.find(nums[i])->second, i };
            }
            m.emplace(target - nums[i], i);
        }
        return {};
    }
};
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
