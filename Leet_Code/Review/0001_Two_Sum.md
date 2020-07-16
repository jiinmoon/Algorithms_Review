[1] Two Sum
===========

Given an array of integers, return **indicies** of the two numbers such that they
add up to a specific target.

You may assume that each input would have **_exactly_** one solution, and you
may not use the _same_ element twice.

**Example**:

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
```

Solution
--------

Naive approach would be to consider every element against each other in
a nested loop. Even with an improvement of not "looking back", the time
complexity of this algorithm is O(n^2).

We may first sort the given array of integers. This gives us a directionality
to use a two pointer method. We will pick two pointers that placed at either
end of the array and consider their elements sum. If the value is less, then we
should move the lower pointer; otherwise, the larger pointer should move down.
The searching itself costs O(n) time  complexity, but the bound on comparison
based sorting limits this algorithm to O(n log(n)).

To improve further, we should trade off our space - that is, we use extra data
structure that allows us to store previously seen elements and look up quickly.
A hashmap allows such operations (where lookup is O(1)). This approach would
allows us to achieve both O(n) in time and spatial complexity.

**Python**

```python
class Solution:
    def find_two_sum(self, nums, target);
        record = dict()
        for i, num in enumerate(nums):
            if num in record:
                return [ record[num], i ]
            record[target - num] = i
        return []
```

**Go**

```Go
func find_two_sum(nums []int, target int) []int {
    var record = make(map[int]int)
    for i, num := range nums {
        record[num] = i
    }
    for i, num := range nums {
        if j, ok := record[target - num]; ok && j != i {
            return []int{i, j}
        }
    }
    return []int{}
}
```




---

LeetCode: [Two Sum](https://leetcode.com/problems/two-sum/)
