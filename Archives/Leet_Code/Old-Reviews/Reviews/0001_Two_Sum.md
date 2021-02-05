1 Two Sum
=========

Question:
---------

Given a narray of integers, return **indicies** of the two numbers such that
they add up to a specific target.

Solutions:
----------

Utilize a dictionary (hashmap) structure to quickly look up the previously seen
values.

Codes:
------

Go:

```go
func twoSum(nums []int, target int) []int {
    var (
        m = make(map[int]int)
    )
    for i, num := range nums {
        if j, ok := m[num]; ok {
            return []int{ j, i }
        }
        m[target - num] = i
    }
    return []int{}
}
```

---

**Source:**

LeetCode: [Two-Sum](https://leetcode.com/problems/two-sum/)
