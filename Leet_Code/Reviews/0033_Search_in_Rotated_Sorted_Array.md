33 Search in Rotated Sorted Array
===================

Question:
---------

Given a sorted array that is rotated about unknown pivot, find the value.

Solutions:
----------

The fact that array still is sorted means that binary search algorithm can be
used to find the value within the array. This is possible since if we divide
the array into equal halves, either lower or upper portion of the array has to
be in the sorted order.

Codes:
------

Go:

```go
func search(nums []int, target int) int {
    var (
        lo = 0
        hi = len(nums)-1
    )
    for lo <= hi {
        mid := lo + (hi - lo) / 2
        if nums[mid] == target {
            return mid
        }

        if nums[lo] <= nums[mid] {
            if nums[lo] <= target && target < nums[mid] {
                hi = mid - 1
            } else {
                lo = mid + 1
            }
            continue
        }
        if nums[mid] < target && target <= nums[hi] {
            lo = mid + 1
        } else {
            hi = mid - 1
        }
    }
    return -1
}
```

---

**Source:**

LeetCode: [Search-in-Rotated-Sorted-Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
