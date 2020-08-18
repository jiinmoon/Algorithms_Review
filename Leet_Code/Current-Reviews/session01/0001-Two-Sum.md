1 Two Sum
=========

Given an array of integers, return **indicies** of the two numbers such that
they add up toa specific target.

You may assume that each input would have **exactly** one solution, and you may
not use the _same_ element twice.

---

Naive approach would be to use the brute force - nested loop where we select
every possible combination of two elements. While is does not use extra spaces,
its time complexity O(n^2).

Slight improvement can be made by first sorting the array. By doing so, it
gives us directionality as to how we can choose our values. For example, when
considering two values and checking their sum, if the sum is less than the
target, then we know that we should move the lower pointer. And vice versa.
Depending on the sorting algorithm, this may take up more space (depends on
whether we are dealing with the array as a value or a pointer) and disrupt the
given array. But the time complexity improves to the lower bound of comparison
sort algorithm O(n * log(n)).

Another approach that can reduce its time complexity to linear time is using
a map structure (hashmap) where we can store the previously seen elements and
check against the new elements as we iterate through.

---

Go: 

A single-pass hashmap approach.

```go
func twoSum(nums []int, target int) []int {
    var m := make(map[int]int)
    for i, num := range nums {
        if j, ok := m[num]; ok {
            return []int{ j, i }
        }
        m[target - num] = i
    }
    return []int{}
}
```

Python:

Sorting approach is used but note that this will not work since the questions
expects to return the original indicies of the target. We sort the copy, but
they would increase it. Below is an example of how we could confirm that there
is a two elements that sums to target.

```python
class Solution:
    def twoSum(self, nums, target):
        nums.sort()
        i, j = 0, len(nums)-1
        while i <= j:
            currSum = nums[i] + nums[j]
            if currSum == target:
                return [i, j]
            if currSum < target:
                i += 1
            else:
                j -= 1
        return []
```


