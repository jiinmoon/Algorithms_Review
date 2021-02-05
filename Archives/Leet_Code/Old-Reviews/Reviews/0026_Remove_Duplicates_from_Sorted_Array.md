26 Remove Duplicates from Sorted Array
======================================

Question:
---------

Given a sorted array _nums_, remove the dulicates in-place such that each
element appear only once and return the new length.

Solutions:
----------

Since the array is already sorted, we know the duplicates elements should be
next to each other. We can maintain an insert pointer where we will move over
the new elements that we encounter to the insert poistion.

Codes:
------

Go:

```go
func removeDuplicates(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    i := 0
    for j := 1; j < len(nums); j++ {
        if nums[i] != nums[j] {
            i += 1
            nums[i] = nums[j]
        }
    }
    return i+1
}
```

---

**Source:**

LeetCode: [Remove-Duplicates-from-Sorted-Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
