# Wave Array

Given an array of integers, sort the array into a wave like array and return
it.

In other words, arrange the elements into a sequence such that a1 >= a2 <= a3
>= a4 <= a5.....

---

### (1) Sort first, then iterate every even element.

By sorting first, we have a sorted array in ascending order where i <= j <=
k <= l ...

Then, by iterating on every even element and swapping them, we can achieve the
wave-sorted array. j >= i <= l >= k <= ...

O(n * log(n)) in time complexity.

### (2) Iterate every even element and compare with previous and next element.

Without sorting, we can simply iterate on every even element and compare
against previous and next.

Suppose we have [1, 2, 3, 4], then first even element encountered is 1. We
do not have previous element but we can compare against next which is 2. It is
out of order so swap to result [2, 1, 3, 4].

Next even element is 3. We compare against prevous element 1 and see that
previous is smaller than current. So we no swap. We compare with next which is
4, and perform swap to result in [2, 1, 4, 3].

O(n) in time complexity. But this has a problem with dealing in lexicographical
order that is imposed.

---

Python: sort.

```python

class Solution:

    def wave(self, arr):

        arr.sort()

        for i in range(0, len(arr)-1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]

        return arr
```
