# Nearest Smallest Element

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

Use stack to maintain the indicies of the elements from behind. For every
element encountered if we found that top of our stack is greater than current
element, then we record the smallest element for index on the top.

O(n) in both time and space complexity.

---

Python:

```python

class Solution:

    def prevSmaller(self, A):

        result = [-1] * len(A)
        stack = []

        for i in range(len(A)-1, -1, -1):
            while stack and A[stack[-1]] > A[i]:
                result[stack.pop()] = A[i]
            stack.append(i)

        return result
```


