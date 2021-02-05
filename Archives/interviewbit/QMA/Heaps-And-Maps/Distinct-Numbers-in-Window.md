# Distinct Numbers in Window

You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return
the of count of distinct numbers in all windows of size B.

Formally, return an array of size N-B+1 where i'th element in this array
contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

NOTE: if B > N, return an empty array.

---

Maintain the count of elements for current window of size B. If the element to
be removed was last, then we decrement distinct element count; if the element
to add was first, we increment distinct element count. For each step, we record
the count of distinct elements present.

O(n) in time complexity and O(n) in space complexity.

---

Python:

```python


from collections import defaultdict

class Solution:

    def distinctNumsInWindow(self, arr, k):

        counter, count = defauldict(int), 0

        # first window
        for i in range(k):
            # first time element is encountered;
            # increment distinct element count
            if arr[i] not in counter:
                count += 1
            counter[arr[i]] += 1

        result = [count]

        # iterate to add/remove each new/last elements
        for i in range(k, len(arr)):
            
            # remove previous arr[i - k]
            count -= counter[arr[i - k]] == 1
            counter[arr[i - k]] -= 1
            
            # add current arr[i]
            count += counter[arr[i]] == 0
            counter[arr[i]] += 1
            
            result.append(count)

        return result

```
