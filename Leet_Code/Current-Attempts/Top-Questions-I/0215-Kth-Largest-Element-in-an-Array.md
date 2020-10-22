# 215 Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

---

Naive solution would be to perform max() operation k number of times to find
the kth largest element - since finding max element in an unsorted array takes
O(n) time, total time complexity should be O(k * n).

Another method would be to simply sort the array and then select the kth
largest element. This is O(n * log(n)) in time complexity.

We may also use variant of Quick Sort called Quick Select - we choose pivot and
partition array left and right of the pivot to find its correct place. This is
repeated K number of times. This can effectivly select the Kth largest element
in O(n) time complexity.

---

Python:

```python

class Solution:
    def findKthLargest(self, nums, k):
        # kth place from behind
        k = len(nums) - k
        l, r = 0, len(nums)-1

        while 1:
            # select pivot and partition array into left and right
            pivot = self.partition(nums, l, r)
            # pivot should be at its rightful place in sorted order
            if pivot == k:
                return nums[pivot]
            if pivot > k:
                r = index - 1
            else:
                l = index + 1

    def partition(self, nums, l, r):
        # there are various ways to select the pivot
        # here we simply use randomized pivot
        pivotIdx = random.randint(l, r)
        pivotVal = nums[pivotIdx]
        # temporary store pivotVal to end of list
        nums[pivotIdx], nums[r] = nums[r], nums[pivotIdx]
        
        # swap values so long as it is less than the pivot
        ins = l
        for i in range(l, r):
            if nums[i] <= pivotVal:
                nums[ins], nums[i] = nums[i], nums[ins]
                ins += 1

        # place pivot back to correct place
        nums[ins], nums[r] = nums[r], nums[ins]
        return ins
```
