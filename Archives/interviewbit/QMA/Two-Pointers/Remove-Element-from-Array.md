# Remove Element from Array

Given an array and a value, remove all the instances of that value in the
array.

Also return the number of elements left in the array after the operation.

It does not matter what is left beyond the expected length.

---

Maintain insertion pointer; so long as the val encountered while iterating on
the given array does not match target, we insert the value unto insertion index
and increment the insertion pointer. O(n) in time complexity and O(1) in space
complexity.

---

Python:

```python

class Solution:

    def removeElement(self, A, B):

        ins = 0
        for num in A:
            if num == B:
                continue
            A[ins] = num
            ins += 1

        return ins
```
