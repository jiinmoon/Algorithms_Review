# 215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

---

#### (1) Sort first.

O(n * log(n)) time complexity approach is to sort the entire unsorted array to
immediately find the k-th largest element at k-th index.

#### (2) Quick Select.

By using modified quick-sort algorithm, we can avoid having to sort the entire
array. At each step, quick-select will partially sort the elements and place
the chosen pivot at its correct place. As we disregard half of the array each
time, time complexity reduces to O(n) from O(n * log(n)).

---

Python: Quick-Select.

```python

from random import randint

class Solution215:

    def findKthLargest(self, nums, k):

        k = len(nums) - k
        l, r = 0, len(nums) - 1

        while True:
            
            pivot = partition(nums, l, r)

            if pivot == k:
                return nums[k]

            elif pivot > k:
                r = pivot - 1

            else:
                l = pivot + 1

    
    def partition(self, nums, l, r):
        # places pivot at its correct position in sorted array
        
        pivot = randint(l, r)
        pivotVal = nums[pivot]

        nums[r], nums[pivot] = nums[pivot], nums[r]

        ins = l
        for i in range(l, r):
            if nums[i] <= pivotVal:
                nums[ins], nums[i] = nums[i], nums[ins]
                ins += 1

        nums[r], nums[ins] = nums[ins], nums[r]

        return ins
```
