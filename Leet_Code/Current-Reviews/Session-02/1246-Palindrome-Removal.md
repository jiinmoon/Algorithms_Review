1246 Palindrome Removal
=======================

Given an integer array arr, in one move you can select a palindromic subarray
and remove that subarray from the given array. Find the minimum number of moves
needed to remove all elements from the array.

---

We need to examine every possible subarray which will take O(n^3) and find
whether the subarray is palindrome or not to remove O(n).

But we may improve upon this design by utilizing memoization. First, let us
consider following cases when we are examining each of the subarray:

1. subarray size 1 can be removed by itself.

2. if last two elements are same, we can remove them in one move and result is
   of the remainder.

3. if any other elements are same as the last, we can remove them and all the
   integers between fro the same cost of removing all elements in between.

For this, we maintain a hashmap structure where we store the result of the each
subarray where (i,j) represents the subarray A[i:j+1] (upto and include j).

Initially, we compute the cost of removing each subarray of size 1.

Then, if for each subarray, if the last two elements are equal, the cost is the
minimum of removing the two elements or the previous result of removing size 1.

After, we iterate between each elements of current subarray. If any of the
element is found to be same as the last element, the min cost is updated to
result of cost of subarray between start to found index plus the cost of found
of index to end of the subarray.

Due to memoization, we should be able to save time on repeated work, and
complete the algorithm in O(n^3).

---

Python:

```python

from functools import lru_cache

class Solution:
    def minimumMoves(self, arr):
        
        @lru_cache(None)
        def helper(i, j):
            # invalid subarray
            if i > j:
                return 0

            # cost of removing subarray of size 1
            minMoves = helper(i, j-1) + 1

            # cost of removing subarray that has last two equal elements
            if arr[j-1] == arr[j]:
                minMoves = min(minMoves, helper(i, j-2) + 1)

            # iterate to find subarr in subarr where elements are equal
            for k in range(i, j-1):
                if arr[j] == arr[k]:
                    minMoves = min(minMoves, helper(i, k-1) + helper(k+1, j-1))

            return minMoves

        return helper(0, len(arr)-1)
```
