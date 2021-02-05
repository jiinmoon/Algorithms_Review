1 Two Sum
=========

To find the two array indicies where their elements sum to a target, first
naive approach that we can consider is brute force method where we will pick an
element and compare it against every other until we find out two values. This
is an O(n^2) time complexity using nested loop.

An improvement can be made by first sorting the array first such that it will
give us a directionality such that we can apply a two pointer method. Since
sorting is involved, at minimum this algorithm is O(n * log(n)).

Best approach is to trade off space to improve time. Here, we can use hashmap
structure to store the previously seen values which we can reference in O(1).
Thus, this algorithm can complete in O(n).

---

C++

```cpp
#include <map>
#include <vector>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (m.find(nums[i]) != m.end())
                return { m.find(nums[i])->second, i };
            m.emplace(target - nums[i], i);
        }
        return {};
    }
}
```
