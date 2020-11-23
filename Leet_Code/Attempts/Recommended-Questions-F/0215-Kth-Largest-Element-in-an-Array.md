# 215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

---

The most efficient element for finding the Kth largest element would be the
modified quick sort algorithm which is quick select. Just as quick sort, we
partition the array about a random (or not smart pivot selection) chosen
element. By doing so, we can repeatedly narrowdown the search space at each
iteration. The time complexity would be O(n).

---

Java:

```java

class Solution {
    
    public int findKthLargest(int[] nums, int k) {
        int l = 0;
        int r = nums.length - 1;

        while (true) {
            int pivot = partition(nums, l, r);
            if (pivot == k)
                return nums[k];
            if (pivot > k) r = pivot - 1;
            else l = pivot + 1;
        }
    }

    public int partition(int[] nums, int l, int r) {
        int pivot = (int) Math.random() * (r - l + 1) + l;
        int pivotVal = nums[pivot];
        nums[pivot] = nums[r]; nums[r] = pivotVal;

        int ins = l;
        for (int i = l; i < r; i++) {
            if (nums[i] <= pivotVal) {
                int temp = nums[ins];
                nums[ins] = nums[i];
                nums[i] = temp;
                ins++;
            }
        }

        nums[r] = nums[ins];
        nums[ins] = pivotVal;
        return ins;
    }
}

```

Python:

```python

class Solution:
    def findKthLargest(self, nums, k):
        # k is the kth place if the nums is in sorted order
        k = len(nums) - k
        l, r = 0, len(nums) - 1
        # repeatedly partition and binary search
        while True:
            pivot = self.partition(nums, l, r)
            # pivot after partition should be in its correct sorted place
            if pivot == k:
                return nums[pivot]
            # else, search upper or lower half
            if pivot > k:
                r = pivot - 1
            else:
                l = pivot + 1

    def partition(self, nums, l, r):
        # here use random selection (or use smart pivot selection)
        pivotIdx = random.randint(l, r)
        pivotVal = nums[pivotIdx]
        # move pivotIdx to last place to save
        nums[pivotIdx], nums[r] = nums[r], nums[pivotIdx]
        
        # swap values between l and r about the chosen pivot val
        ins = l
        for i in range(l, r):
            if nums[i] <= pivotVal:
                nums[ins], nums[i] = nums[i], nums[ins]
                ins += 1

        # place the pivotVal back to its correct place
        nums[ins], nums[r] = nums[r], nums[ins]
        return ins
```
