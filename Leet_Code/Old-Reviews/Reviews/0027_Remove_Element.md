27 Remove Element
=================

Question:
---------

Given an array _nums_ and a value _val_, remove all instances of that value
in-place and return the new length.

Solutions:
----------

As we enumerate on the given array, whenever we encounter value that is not
_val_, we move it over to the insert position.

Codes:
------

Go:

```go
func removeElement(nums []int, val int) int {
    i := 0
    for _, num := range nums {
        if num != val {
            nums[i] = num
            i++
        }
    }
    return i
}
```

---

**Source:**

LeetCode: [Remove-Element](https://leetcode.com/problems/remove-element/)
