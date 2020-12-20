# Nearest Smaller Element

    Given an array, find the nearest smaller element G[i] for every element A[i] in
    the array such that the element has an index smaller than i.

    More formally,

    G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
    Elements for which no smaller element exist, consider next
    smaller element as -1.

---

## Approach:

We use stack to maintain the previous values that we have seen. For every
element that we examine, we check against the top of our stack; if we found
that current element is smaller than the what is on top of our stack, then the
nearest smaller element for top of our stack has to be current element.

O(n) in both time and space complexity.

---

Python:

```python

class Solution:

    def nearestSmallerElement(self, nums):

        result = [-1] * len(nums)
        stack = []

        for i in range(len(nums)-1, -1, -1):

            while stack and nums[stack[-1]] > nums[i]:
                result[stack.pop()] = nums[i]

            stack.append(i)

        return result

```

