# 1570. Dot Product of Two Sparse Vectors

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector
and vec
A sparse vector is a vector that has mostly zero values, you should store the
sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

---

Naive way to implement would be to treat this simply as an array of nums
- vectors. Then, for given vector, we iterate to create dot product sum of all
  the values. This is least efficient method that much needs to be improved
  upon.

Further improvement can be made by noticing that we are dealing with sparse
vectors. As most values will be 0, we can first spend O(n) time complexity
during construction to create only the index: number map for given initial
vector so long as the number is not zero. Thus, we can reduce the time
complexity on average case given that the vectors are gurantee'd to be sparse
by saving only the non-zero values and its indicies.

---

Python:

```python

class SparseVector:
    def __init__(self, nums):
        self.d = {i:num for i, num in enumerate(nums)}

    def dotProduct(self, vec):
        result = 0
        for key in vec.d.keys():
            if key in self.d:
                result += vec.d[key] * self.d[key]
        return result
```
